#!/bin/bash -e

ETCD=/usr/local/bin/etcdctl

type jq >/dev/null 2>&1 || ( echo "Jq is not installed" ; exit 1 )
type curl >/dev/null 2>&1 || ( echo "Curl is not installed" ; exit 1 )

# get etcd members credentials
MEMBERS="${ETCD} --endpoints https://127.0.0.1:2379 member list"
LEADER_ID=$(eval "$MEMBERS" | awk -F ':' '/isLeader=true/ {print $1}')
LEADER_ENDPOINT=$(eval "$MEMBERS" | awk '/isLeader=true/ {print $4}' | cut -d"=" -f2)
SLAVE_ID=$(eval "$MEMBERS" | grep 'isLeader=false' | head -n 1 | awk -F ":" '{print $1}')
SLAVE_ENDPOINT=$(eval "$MEMBERS" | grep 'isLeader=false' | head -n 1 | awk '{print $4}' | cut -d"=" -f2)

# member count:
metric_members_count=`curl -s -k https://172.20.9.15:2379/v2/members | jq -c '.members | length'`
metric_total_keys_count=`${ETCD} --endpoints https://127.0.0.1:2379 ls -r --sort | wc -l`
metric_total_size_dataset=`pidof etcd | xargs ps -o rss | awk '{rss=+$1} END {print rss}'`
metric_store_stats=`curl -s -k ${LEADER_ENDPOINT}/v2/stats/store| tr -d \"\{\} | sed -e 's/:/=/g'`
metric_latency_from_leader_avg=`curl -s -k ${LEADER_ENDPOINT}/v2/stats/leader | \
                                jq -c ".followers.\"${SLAVE_ID}\".latency.average"`
metric_leader_stats=`curl -s -k ${LEADER_ENDPOINT}/v2/stats/self | \
                                jq -c "{ sendBandwidthRate: .sendBandwidthRate, sendAppendRequestCnt: \
                                .sendAppendRequestCnt, sendPkgRate: .sendPkgRate }"| tr -d \"\{\} | sed -e 's/:/=/g'`
metric_slave_stats=`curl -s -k ${SLAVE_ENDPOINT}/v2/stats/self | \
                                jq -c "{ recvBandwidthRate: .recvBandwidthRate, recvAppendRequestCnt: \
                                .recvAppendRequestCnt, recvPkgRate: .recvPkgRate }"| tr -d \"\{\} | sed -e 's/:/=/g'`
cat << EOF
etcd_general_stats,group=etcd_cluster_metrics members_count=${metric_members_count},dataset_size=${metric_total_size_dataset},total_keys_count=${metric_total_keys_count}
etcd_leader_stats,group=etcd_cluster_metrics $metric_leader_stats
etcd_follower_stats,group=etcd_cluster_metrics ${metric_slave_stats},latency_from_leader_avg=${metric_latency_from_leader_avg}
etcd_store_stats,group=etcd_cluster_metrics $metric_store_stats
EOF
