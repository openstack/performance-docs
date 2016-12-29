#!/bin/bash -e


K8S_MASTER=127.0.0.1

if [[ $1 ]] ; then
    K8S_MASTER=$1
fi

type jq >/dev/null 2>&1 || ( echo "Jq is not installed" ; exit 1 )
type curl >/dev/null 2>&1 || ( echo "Curl is not installed" ; exit 1 )

curl_get() {
    url="https://${K8S_MASTER}$@"
    curl -k -s -u kube:changeme $url || ( echo "Curl failed at: $url" 1>&2; exit 1 )
}
# gathering frequent API calls output to separate file(in order to avoid long timeouts):
node_file=`mktemp /tmp/XXXXX`
pods_file=`mktemp /tmp/XXXXX`
endpoints_file=`mktemp /tmp/XXXXX`
curl_get "/api/v1/nodes" > $node_file
curl_get "/api/v1/pods" > $pods_file
curl_get "/api/v1/endpoints" > $endpoints_file
# metrics withdrawal:
number_of_namespaces_total=`curl_get "/api/v1/namespaces" | jq '[ .items[] .metadata.name ] | length'`
number_of_services_total=`curl_get "/api/v1/services" | jq -c '[ .items[] .metadata.name ] | length'`
number_of_nodes_total=`jq -c '[ .items[] .metadata.name ] | length' $node_file`
number_of_unsched=`jq -c '[ .items[] | select(.spec.unschedulable != null) .metadata.name ] | length' $node_file`
number_in_each_status=`jq -c '[ .items[] | .status.conditions[] | select(.type == "Ready") .status \
                    | gsub("(?<a>.+)"; "number_of_status_\(.a)" ) ] | group_by(.) | map({(.[0]): length}) | add ' $node_file \
                    | tr -d \"\{\} | sed -e 's/:/=/g'`
number_of_pods_total=`jq -c '[ .items[] .metadata.name ] | length' $pods_file`
number_of_pods_state_Pending=`jq -c '[ .items[] .status.phase | select(. == "Pending")] | length' $pods_file`
number_of_pods_state_Running=`jq -c '[ .items[] .status.phase | select(. == "Running")] | length' $pods_file`
number_of_pods_state_Succeeded=`jq -c '[ .items[] .status.phase | select(. == "Succeeded")] | length' $pods_file`
number_of_pods_state_Failed=`jq -c '[ .items[] .status.phase | select(. == "Failed")] | length' $pods_file`
number_of_pods_state_Unknown=`jq -c '[ .items[] .status.phase | select(. == "Unknown")] | length' $pods_file`
number_of_pods_per_node=`jq -c '[ .items[] | .spec.nodeName ] | group_by(.) | \
                    map("k8s_pods_per_node,group=k8s_cluster_metrics,pod_node=\(.[0]) value=\(length)")' $pods_file \
                    | sed -e 's/\["//g' -e 's/"\]//g' -e 's/","/\n/g'`
number_of_pods_per_ns=`jq -c '[ .items[] | .metadata.namespace ] | group_by(.) | \
                    map("k8s_pods_per_namespace,group=k8s_cluster_metrics,ns=\(.[0]) value=\(length)")' $pods_file \
                    | sed -e 's/\["//g' -e 's/"\]//g' -e 's/","/\n/g'`
number_of_endpoints_each_service=`jq -c '[ .items[] | { service: .metadata.name, endpoints: .subsets[] } | \
                    . as { service: $svc, endpoints: $endp } | $endp.addresses | length | . as $addr | $endp.ports | length | \
                    . as $prts | "k8s_services,group=k8s_cluster_metrics,service=\($svc) endpoints_number=\($addr * $prts)" ] ' $endpoints_file \
                    | sed -e 's/\["//g' -e 's/"\]//g' -e 's/","/\n/g'`
number_of_endpoints_total=`jq -c '[ .items[] | .subsets[] | { addrs: .addresses, ports: .ports } \
                    | map (length ) | .[0] * .[1] ] | add' $endpoints_file`
number_of_API_instances=`curl_get "/api/" |  jq -c '.serverAddressByClientCIDRs | length'`
number_of_controllers=`curl_get "/api/v1/replicationcontrollers" | jq '.items | length'`
number_of_scheduler_instances=`curl_get /api/v1/namespaces/kube-system/pods?labelSelector='k8s-app=kube-scheduler' \
                    | jq -c '.items | length' `
cluster_resources_CPU=`jq -c '[ .items[] .status.capacity.cpu | tonumber ] | add' $node_file`
cluster_resources_RAM=`jq -c '[ .items[] .status.capacity.memory| gsub("[a-z]+$"; "" ; "i") | tonumber] | add' $node_file`

# output:
cat << EOF
k8s_nodes,group=k8s_cluster_metrics number_of_nodes_total=${number_of_nodes_total},number_of_unsched=${number_of_unsched}
k8s_nodes_states,group=k8s_cluster_metrics ${number_in_each_status}
k8s_namespaces,group=k8s_cluster_metrics number_of_namespaces_total=${number_of_namespaces_total}
k8s_pods,group=k8s_cluster_metrics number_of_pods_total=${number_of_pods_total}
k8s_pods_states,group=k8s_cluster_metrics number_of_pods_state_Pending=${number_of_pods_state_Pending},number_of_pods_state_Running=${number_of_pods_state_Running},number_of_pods_state_Succeeded=${number_of_pods_state_Succeeded},number_of_pods_state_Failed=${number_of_pods_state_Failed},number_of_pods_state_Unknown=${number_of_pods_state_Unknown}
${number_of_pods_per_node}
${number_of_pods_per_ns}
${number_of_endpoints_each_service}
k8s_services,group=k8s_cluster_metrics number_of_services_total=${number_of_services_total},number_of_endpoints_total=${number_of_endpoints_total}
k8s_number_of_API_instances,group=k8s_cluster_metrics value=${number_of_API_instances}
k8s_number_of_controllers,group=k8s_cluster_metrics value=${number_of_controllers}
k8s_number_of_scheduler_instances,group=k8s_cluster_metrics value=${number_of_scheduler_instances}
k8s_cluster_resources,group=k8s_cluster_metrics cpu_total=${cluster_resources_CPU},ram_total=${cluster_resources_RAM}
EOF

# cleanup
rm -f $node_file $pods_file $endpoints_file
