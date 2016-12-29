#!/bin/bash
# output from iostat -Ndx is
# Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
export LANG=C
iostat -Ndx | tail -n +4 | head -n -1 | awk '{print "system_per_device_iostat,device="$1" read_merge="$2",write_merge="$3",await="$10",read_await="$11",write_await="$12",util="$14",average_queue="$9}'

