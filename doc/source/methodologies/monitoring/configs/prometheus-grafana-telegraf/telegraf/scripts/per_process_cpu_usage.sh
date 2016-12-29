#!/bin/bash
export LANG=C
for i in $(ps --no-headers -A -o pid); do
   pidstat -p $i | tail -n 1 | grep -v PID | awk '{print "system_per_process_cpu_usage,process="$9" user="$4",system="$5}'
done

