#!/bin/bash
export LANG=C
IFS='
'
SUM_RESV_Q=0
SUM_SEND_Q=0
for i in $(netstat -4 -n); do
   RESV_Q=$(echo $i | awk '{print $2}')
   SEND_Q=$(echo $i | awk '{print $3}')
   SUM_RESV_Q=$((${SUM_RESV_Q} + ${RESV_Q}))
   SUM_SEND_Q=$((${SUM_SEND_Q} + ${SEND_Q}))
done
echo "system_tcp_queue sum_recv=${SUM_RESV_Q},sum_send=${SUM_SEND_Q}"
