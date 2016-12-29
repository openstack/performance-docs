#!/bin/bash
# Variables declaration
WORKDIR="$(cd "$(dirname ${0})" && pwd)"
OS_LOG_PARSER="${WORKDIR}/glog.sh"
TMPDATADIR="${WORKDIR}/data"
TMP_METRICS="${TMPDATADIR}/allmetrics.tmp"
MODE="${MODE:-bg}"
SCRIPT_LOG_DIR="${WORKDIR}/logs"
SCRIPT_LOG_FILE="${SCRIPT_LOG_DIR}/run_results_$(date +%Y-%m-%d).log"
SCRIPT_LOG_LVL=2
K8S_NS="${K8S_NS:-ccp}"
declare -a OSCONTROLLER=(
'cinder-api:1,2,21'
'glance-api:1,2,22'
'heat-api:1,2,22'
'neutron-metadata-agent:1,2,17'
'neutron-server:1,2,22'
'nova-api:1,2,21'
'keystone:4,5,11'
)
declare -a OSCOMPUTE=(
'nova-compute:'
)
# crete subfolder under working directory
function mk_dir()
{
  local newdir="${TMPDATADIR}/${1}"
  if [ ! -d "${newdir}" ]; then
    mkdir -p ${newdir}
  fi
}
# log function
function log()
{
  local input
  local dtstamp
  input="$*"
  dtstamp="$(date +%Y-%m-%d_%H%M%S)"
  if [ ! -d "${SCRIPT_LOG_DIR}" ]; then
    mkdir -p "${SCRIPT_LOG_DIR}"
  fi
  case "${SCRIPT_LOG_LVL}" in
    3)
      if [ ! -z "${input}" ]; then
        echo "${dtstamp}: ${input}" | tee -a "${SCRIPT_LOG_FILE}"
      fi
      ;;
    2)
      if [ ! -z "${input}" ]; then
        echo "${dtstamp}: ${input}" >> "${SCRIPT_LOG_FILE}"
      fi
      ;;
    1)
      if [ ! -z "${input}" ]; then
        echo "${dtstamp}: ${input}"
      fi
      ;;
    *)
      ;;
  esac
}
# get roles according to predefined in OSCONTROLLER & OSCOMPUTE
function get_role()
{
  local role
  local input
  local arr_name
  local arr_name_fields
  role=${1}
  shift
  input=$*
  case ${role} in
    "controller")
      for i in $(seq 0 $(( ${#OSCONTROLLER[@]} - 1)))
      do
        arr_name=$(echo ${OSCONTROLLER[${i}]} | cut -d":" -f1)
        arr_name_fields=$(echo ${OSCONTROLLER[${i}]} | cut -d":" -f2)
        if [[ "${arr_name}" == "${input}" ]]; then
          echo "${arr_name_fields}"
          return 0
        fi
      done
      ;;
    "compute")
      for i in $(seq 0 $(( ${#OSCOMPUTE[@]} - 1)))
      do
        arr_name=$(echo ${OSCOMPUTE[${i}]} | cut -d":" -f1)
        arr_name_fields=$(echo ${OSCOMPUTE[${i}]} | cut -d":" -f2)
        if [ "${arr_name}" == "${input}" ]; then
          echo "${arr_name_fields}"
          return 0
        fi
      done
      ;;
  esac
  return 1
}
# diff in seconds
function tdiff()
{
  local now
  local datetime
  local result
  datetime="$(date -d "${1}" +%s)"
  now="$(date +%s)"
  result=$(( ${now} - ${datetime} ))
  echo ${result}
}
# lock file function
function glock()
{
  local action
  local lockfile
  local accessdate
  local old_in_sec=120
  action="${1}"
  # lockfile="${TMP_METRICS}.lock"
  lockfile="${TMPDATADIR}/allmetrics.tmp.lock"
  if [[ "${action}" == "lock" && ! -e "${lockfile}" ]]; then
    touch "${lockfile}"
  elif [[ "${action}" == "lock" && -e "${lockfile}" ]]; then
    accessdate="$(stat ${lockfile} | grep Modify | cut -d' ' -f2,3)"
    if [ "$(tdiff "${accessdate}")" -ge "${old_in_sec}" ]; then
      rm "${lockfile}"
      touch "${lockfile}"
    else
      log "Lock file ${lockfile} exists!"
      return 1
    fi
  else
    rm "${lockfile}"
  fi
  return 0
}
# wait for parcers launched in backgroud mode
function gatherchildren()
{
  local childrencount
  while true
  do
    childrencount=$(ps axf| grep ${OS_LOG_PARSER} | grep -v grep | wc -l)
    if [ "${childrencount}" -eq 0 ]; then
      return
    fi
    log "Children running ${childrencount}."
    sleep 1
  done
}
# list of running contaners
function get_k8s_containers()
{
  local cont_host
  local cont_pod
  local cont_name
  local cont_id
  local os_log_fields
  local cont_tmp_dir
  local _raw_data
  glock "lock"
  if [ "$?" -ne 0 ]; then exit 1;fi
  #echo '[' > ${TMP_METRICS}
  _raw_data="${TMPDATADIR}/._raw_data"
  rm -rf ${_raw_data}
  kubectl get pods -n "${K8S_NS}" -o 'go-template={{range .items}}{{if or (ne .status.phase "Succeeded")  (eq .status.phase "Running")}}{{.spec.nodeName}},{{.metadata.name}},{{range .status.containerStatuses}}{{.name}},{{.containerID}}{{end}}{{"\n"}}{{end}}{{end}}' > ${_raw_data}
  for data in $(cat ${_raw_data})
  do
    cont_host=$(echo ${data} | cut -d',' -f1)
    cont_pod=$(echo ${data} | cut -d',' -f2)
    cont_name=$(echo ${data} | cut -d',' -f3)
    cont_id=$(echo ${data} | cut -d',' -f4 | sed 's|^docker://||')
    cont_tmp_dir="${cont_host}_${cont_pod}_${cont_name}"
    os_log_fields=$(get_role "controller" "${cont_name}")
    if [ "$?" -eq 0  ]; then
      mk_dir "${cont_tmp_dir}"
      export K8S_NS=${K8S_NS}
      export TMP_DIR=${TMPDATADIR}/${cont_tmp_dir}
      # export TMP_METRICS=${TMP_METRICS}
      export TMP_METRICS="${TMPDATADIR}/results/${cont_pod}.tmp"
      export CONTID=${cont_id}
      export CONTAINER=${cont_name}
      export HOST=${cont_host}
      export POD=${cont_pod}
      export OS_LOG_FIELDS=${os_log_fields}
      log "MODE=${MODE} CONTID=${cont_id} TMP_METRICS=${TMP_METRICS} ROLE=controller HOST=${cont_host} POD=${cont_pod} CONTAINER=${cont_name} OS_LOG_FIELDS=${os_log_fields} TMP_DIR=${TMPDATADIR}/${cont_tmp_dir}  K8S_NS=${K8S_NS} ${OS_LOG_PARSER}"
      if [[ "${MODE}" == "bg" ]]; then
        log "${cont_pod} ${cont_name} ${cont_id}"
        ${OS_LOG_PARSER} &
      else
        ${OS_LOG_PARSER}
      fi
    unset TMP_METRICS
    unset CONTID
    unset CONTAINER
    unset POD
    unset OS_LOG_FIELDS
    unset HOST
    fi
    # os_log_fields=$(get_role "compute" "${cont_name}")
    # if [ "$?" -eq 0 ]; then
    #   mk_dir "${cont_tmp_dir}"
    #   log "ROLE=compute HOST=${cont_host} POD=${cont_pod} CONTAINER=${cont_name} OS_LOG_FIELDS=${os_log_fields} TMP_DIR=${TMPDATADIR}/${cont_tmp_dir} K8S_NS=${K8S_NS} ${OS_LOG_PARSER}"
    # fi
  done
  gatherchildren
  if [ "$(ls ${TMPDATADIR}/results/ | wc -l)" -gt 0 ]; then
    cat ${TMPDATADIR}/results/*.tmp
    log "Resulting lines $(cat ${TMPDATADIR}/results/*.tmp | wc -l)"
    rm -rf ${TMPDATADIR}/results/*
  fi
  glock "unlock"
}
# Main logic
mk_dir
mk_dir "results"
get_k8s_containers
