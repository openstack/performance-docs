#!/bin/bash
# Script for IO testing
WORKDIR="$(cd "$(dirname ${0})" && pwd)"
WORKSPACE="${WORKDIR}/workspace"
USER_NAME="${USER_NAME:-root}"
USER_PASS="${USER_PASS:-r00tme}"
REMOTE_HOST="${REMOTE_HOST:-172.20.9.15}"
STARTTIME=""
STOPTIME=""
function prepare()
{
  local ec=0
  mkdir -p ${WORKSPACE}
  export DEBIAN_FRONTEND=noninteractive
  apt update > /dev/null 2>&1 || ec=$?
  apt install -y fio sshpass bc > /dev/null 2>&1 || ec=$?
  return ${ec}
}

function check_vol()
{
  local volpath
  local retval
  local maxretry
  local counter
  retval=1
  counter=0
  maxretry=60
  volpath=${TARGET}
  while true
  do
    if [ -e ${volpath} ]; then
      retval=0
      break
    else
      continue
    fi
    counter=$(( counter + 1 ))
    sleep 2
    if [ "${counter}" -ge "${maxretry}" ]; then
      break
    fi
  done
  return ${retval}
}

function u2m_sec()
{
  local input
  local output
  input=${1}
  output=$(echo "scale=4;${input}/1000" | bc)
  if echo ${output} | grep -q '^\..'; then
    output="0${output}"
  fi
  echo "${output}"
}

parse_terse()
{
  # msec = 1000 usec, 1s = 1000 msec
  local input=$*
  local jobname #3
  local read_iops #8
  local read_bw #7 #KB/s
  local read_clat_min #14 #usec
  local read_clat_max #15 #usec
  local read_clat_mean #16 #usec
  local read_clat_95 #29 #usec
  local read_clat_99 #30 #usec
  local read_total_lat_avg #40 #usec
  local read_bw_avg #45 #KB/s
  local write_iops #49
  local write_bw #48 #KB/s
  local write_clat_min #55 #usec
  local write_clat_max #56 #usec
  local write_clat_mean #57 #usec
  local read_clat_95 #70 #usec
  local read_clat_99 #71 #usec
  local write_total_lat_avg #81 #usec
  local write_bw_avg #86 #KB/s
  jobname="$(echo "${input}" | cut -d';' -f3)"
  read_iops="$(echo "${input}" | cut -d';' -f8)"
  read_bw="$(echo "${input}" | cut -d';' -f7)"
  read_clat_min="$(u2m_sec "$(echo "${input}" | cut -d';' -f14)")"
  read_clat_max="$(u2m_sec "$(echo "${input}" | cut -d';' -f15)")"
  read_clat_mean="$(u2m_sec "$(echo "${input}" | cut -d';' -f16)")"
  read_clat_95="$(u2m_sec "$(echo "${input}" | cut -d';' -f29 | cut -d'=' -f2)")"
  read_clat_99="$(u2m_sec "$(echo "${input}" | cut -d';' -f30 | cut -d'=' -f2)")"
  read_total_lat_avg="$(u2m_sec "$(echo "${input}" | cut -d';' -f40)")"
  read_bw_avg="$(echo "${input}" | cut -d';' -f45)"
  write_iops="$(echo "${input}" | cut -d';' -f49)"
  write_bw="$(echo "${input}" | cut -d';' -f48)"
  write_clat_min="$(u2m_sec "$(echo "${input}" | cut -d';' -f55)")"
  write_clat_max="$(u2m_sec "$(echo "${input}" | cut -d';' -f56)")"
  write_clat_mean="$(u2m_sec "$(echo "${input}" | cut -d';' -f57)")"
  write_clat_95="$(u2m_sec "$(echo "${input}" | cut -d';' -f70 | cut -d'=' -f2)")"
  write_clat_99="$(u2m_sec "$(echo "${input}" | cut -d';' -f71 | cut -d'=' -f2)")"
  write_total_lat_avg="$(u2m_sec "$(echo "${input}" | cut -d';' -f81)")"
  write_bw_avg="$(echo "${input}" | cut -d';' -f86)"
  echo "${STARTTIME},${STOPTIME},${jobname},${read_iops},${read_bw},${read_clat_mean},${read_clat_min},${read_clat_max},${read_clat_95},${read_clat_99},${read_total_lat_avg},${read_bw_avg},${write_iops},${write_bw},${write_clat_mean},${write_clat_min},${write_clat_max},${write_clat_95},${write_clat_99},${write_total_lat_avg},${write_bw_avg}"
}

function run_fio()
{
  local iodepth
  local bs
  local ioengine
  local direct
  local buffered
  local jobname
  local filename
  local size
  local readwrite
  local runtime
  bs="4k"
  direct=1
  buffered=0
  ioengine="libaio"
  jobname="$(hostname)_fio"
  iodepth="${IODEPTH}"
  filename="${TARGET}"
  size="--size=${SIZE}"
  readwrite="${RWMODE}"
  STARTTIME=$(date +%Y.%m.%d-%H:%M:%S)
  if [[ "${RUNMOD}" == "time" ]]; then runtime="--runtime=${RUNTIME} --time_based=1"; size='';fi
  fio --ioengine=${ioengine} --direct=${direct} --buffered=${buffered} \
  --name=${jobname} --filename=${filename} --bs=${bs} --iodepth=${iodepth} ${size} \
  --readwrite=${readwrite} ${runtime} --output-format=terse --terse-version=3 --output=${WORKSPACE}/"$(hostname)"_terse.out 2>&1 | tee ${WORKSPACE}/"$(hostname)"_raw_fio_terse.log
  STOPTIME="$(date +%Y.%m.%d-%H:%M:%S)"
  if [ "$(stat ${WORKSPACE}/"$(hostname)"_raw_fio_terse.log | grep -oP '(?<=(Size:))(.[0-9]+\s)')" -eq 0 ]; then
    rm ${WORKSPACE}/"$(hostname)"_raw_fio_terse.log
  fi
}

function put_results()
{
  local remotehost
  local remotepath
  remotehost="${1}"
  remotepath="/${USER_NAME}/results"
  if [ -f ${WORKSPACE}/"$(hostname)"_results.csv ]; then
    sshpass -p ${USER_PASS} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ${USER_NAME}@${remotehost} "mkdir -p ${remotepath}"
    sshpass -p ${USER_PASS} scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -r ${WORKSPACE}/*.* ${USER_NAME}@${remotehost}:${remotepath}/
  else
    exit 1
  fi
}

# Main
IODEPTH="${IODEPTH:-64}"
TARGET="${TARGET:-/dev/vdc}"
SIZE="${SIZE:-4G}"
RUNTIME="${RUNTIME:-600}" # 10min
RWMODE="${RWMODE:-randrw}"
RUNMOD="${RUNMOD}"
PARSEONLY="${PARSEONLY:-false}"

# Output format:
# starttime, endtime, Jobname, read IOPS, read bandwith KB/s, mean read complete latency msec, avg read latency msec, avg read bandwith KB/s, write IOPS, write bandwith KB/s, mean write complete latency msec, avg write latency msec, avg write bandwith KB/s
if [[ "${PARSEONLY}" == "true" ]]; then
  for tline in $(cat "${1}")
  do
    parse_terse "${tline}"
  done
  exit 0
fi
prepare || exit $?
check_vol || exit $?
run_fio
parse_terse "$(cat ${WORKSPACE}/"$(hostname)"_terse.out)" > ${WORKSPACE}/"$(hostname)"_results.csv
put_results "${REMOTE_HOST}"
