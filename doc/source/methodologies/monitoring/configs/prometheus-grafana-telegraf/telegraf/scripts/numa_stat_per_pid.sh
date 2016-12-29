#!/bin/bash
set -o nounset                              # Treat unset variables as an error
#set -x
export LANG=C
if [ ! -d '/sys/devices/system/node' ]; then
   # This host does not have NUMA
   exit 44
fi
ALL_PROCESS="$(ps --no-headers -A -o pid,ucomm)"
for i in $(echo "${ALL_PROCESS}" | awk '{print $1}'); do
   if [ -f "/proc/$i/numa_maps" ]; then
     NUM_STAT=$(numastat -p $i)
     PROC_NAME=$(echo "${ALL_PROCESS}" | grep -E "( $i |^$i )" | awk '{print $2}')
     echo "${NUM_STAT}" | grep Huge | awk -v p=$i -v n=$PROC_NAME \
      '{printf "system_numa_memory_per_pid,pid="p",name="n" memory_huge="$NF","}'
     echo "${NUM_STAT}" | grep Heap | awk '{printf "memory_heap="$NF","}'
     echo "${NUM_STAT}" | grep Stack | awk '{printf "memory_stack="$NF","}'
     echo "${NUM_STAT}" | grep Private | awk '{print "memory_private="$NF}'
   fi
done


