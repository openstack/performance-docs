#!/bin/bash -e

if [[ ! $1 ]] || [[ ! $2 ]] ; then
    echo \$1 = kargo_env_name, \$2 = csv file path
    exit 1
fi

WORKDIR='~/worked_up_results/'
cur_dir="${WORKDIR}kargo_${1}"
csv_name=`basename $2`
if [[ ! -d $cur_dir ]] ; then mkdir -p $cur_dir ; fi

awk -F "," 'BEGIN {getline;getline;getline;getline;getline;getline;getline;
    print "time,cpu_usage,ram_usage,net_recv,net_send,net_all,dsk_io_read,dsk_io_writ,dsk_all"}
    {printf "%s,%0.3f,%0.3f,%0.3f,%0.3f,%0.3f,%d,%d,%d\n", $1,100-$4,$8/1048576,$12/8,$13/8,($12+$13)/8,$14,$15,$14+$15 }' $2 > $cur_dir/${csv_name}

