#!/bin/bash
# Output in MB/s
# echo 0 > /proc/sys/kernel/nmi_watchdog
# modprobe msr
export LANG=C
MEM_BW=$(sudo /opt/telegraf/bin/pcm-memory-one-line.x /csv 1 2>/dev/null | tail -n 1 | awk '{print $28}')
echo "system_memory bandwidth=${MEM_BW}"