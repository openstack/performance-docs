#!/bin/bash
# Logs extractor / parser
# checking that we are good
if [[ -z "${TMP_DIR}" || -z "${POD}" || -z "${CONTAINER}" || -z "${K8S_NS}" || -z "${OS_LOG_FIELDS}" || -z ${CONTID} ]]; then
  echo "Required variables are not set, exiting!"
  exit 1
fi
# Variables declaration
SSH_USER="${SSH_USER:-root}"
SSH_PASS="${SSH_PASS:-r00tme}"
LOG_ENTRIES_NUMBER=${LOG_ENTRIES_NUMBER:-1000}
LAST_TIME_STAMP_FILE="${TMP_DIR}/timestamp.tmp"
# get | set last timestamp for log entries
function last_ts_data()
{
  local action
  action=${1}
  shift
  if [ "${action}" == "get" ]; then
    if [ -e ${LAST_TIME_STAMP_FILE} ]; then
      cat ${LAST_TIME_STAMP_FILE}
    fi
  else
    echo "$*" > ${LAST_TIME_STAMP_FILE}
  fi
}
function print_out()
{
  if [ -z "${TMP_METRICS}" ];then
    echo "$@"
  else
    echo "$@" >> ${TMP_METRICS}
  fi
}
function micro_to_seconds()
{
  local input
  local output
  input="${1}"
  output=$(echo "scale=4;${input}/1000000" | bc)
  if echo ${output} | grep -q '^\..'; then
    output="0${output}"
  fi
  echo "${output}"
}
# extract container logs from k8s
function get_logs()
{
  local sdate
  local stime
  local scalltime
  local lasttimestamp
  local is_foundlast
  local tmpdata
  tmpdata="${TMP_DIR}/tmpdata.log"
  if [ -e "${tmpdata}" ]; then rm -f ${tmpdata}; fi
    if [ "${CONTAINER}" == "keystone" ];then
      sshpass -p ${SSH_PASS} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ${SSH_USER}@${HOST} "tail -n${LOG_ENTRIES_NUMBER} /var/log/ccp/keystone/keystone-access.log | cut -d' ' -f${OS_LOG_FIELDS} | sed -e 's#\[##g' -e 's#\]##g'" 2>/dev/null > ${tmpdata}
    else
      sshpass -p ${SSH_PASS} ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no ${SSH_USER}@${HOST} "docker logs --tail ${LOG_ENTRIES_NUMBER} ${CONTID} 2>&1 | grep 'INFO' | grep 'GET /' | cut -d' ' -f${OS_LOG_FIELDS}" 2>/dev/null > ${tmpdata}
    fi
  is_foundlast=false
  lasttimestamp=$(last_ts_data "get")
  if [ -z "${lasttimestamp}" ]; then
  while read log
  do
    sdate=$(echo ${log} | cut -d' ' -f1)
    stime=$(echo ${log} | cut -d' ' -f2)
    scalltime=$(echo ${log} | cut -d' ' -f3)
    if [ "${CONTAINER}" == "keystone" ];then scalltime=$(micro_to_seconds ${scalltime});fi
    if [ ! -z "${scalltime}" ]; then
      print_out "os_api_response_time,container=${CONTAINER},pod=${POD},instance=${HOST},requestdate=${sdate},requesttime=${stime} processingtime=${scalltime}"
    fi
  done < <(cat ${tmpdata})
    sdate=$(tail -n 1 ${tmpdata} | cut -d' ' -f1)
    stime=$(tail -n 1 ${tmpdata} | cut -d' ' -f2)
    last_ts_data "set" "${sdate}${stime}"
  else
    while read log
    do
      sdate=$(echo ${log} | cut -d' ' -f1)
      stime=$(echo ${log} | cut -d' ' -f2)
      scalltime=$(echo ${log} | cut -d' ' -f3)
      if [ "${CONTAINER}" == "keystone" ];then scalltime=$(micro_to_seconds ${scalltime});fi
      if [[ "${is_foundlast}" = "false"  && "${lasttimestamp}" = "${sdate}${stime}" ]]; then
        #echo "FOUND: ${sdate}${stime} ${scalltime}"
        is_foundlast=true
        continue
      fi
      if [ "${is_foundlast}" == "true" ]; then
        if [ ! -z "${scalltime}" ]; then
          print_out "os_api_response_time,container=${CONTAINER},pod=${POD},instance=${HOST},requestdate=${sdate},requesttime=${stime} processingtime=${scalltime}"
        fi
      fi
    done < <(cat ${tmpdata})
    if [ "${is_foundlast}" == "true" ]; then
      sdate=$(tail -n 1 ${tmpdata} | cut -d' ' -f1)
      stime=$(tail -n 1 ${tmpdata} | cut -d' ' -f2)
      last_ts_data "set" "${sdate}${stime}"
    fi
  fi
  rm -f ${tmpdata}
}
# Main logic
get_logs
