#!/bin/bash
export LANG=C
set -o nounset                              # Treat unset variables as an error
echo "system entropy=$(cat /proc/sys/kernel/random/entropy_avail)"

