#!/bin/bash
set -u -e

function escape_test_name() {
    sed 's/[]\$*.^|()[]/\\&/g; s/\s\+/\\s+/g' <<< "$1" | tr -d '\n'
}

TESTS_TO_SKIP=(
    '[k8s.io] Port forwarding [k8s.io] With a server that expects no client request should support a client that connects, sends no data, and disconnects [Conformance]'
    '[k8s.io] Port forwarding [k8s.io] With a server that expects a client request should support a client that connects, sends no data, and disconnects [Conformance]'
    '[k8s.io] Port forwarding [k8s.io] With a server that expects a client request should support a client that connects, sends data, and disconnects [Conformance]'
    '[k8s.io] Downward API volume should update annotations on modification [Conformance]'
    '[k8s.io] DNS should provide DNS for services [Conformance]'
    '[k8s.io] Load capacity [Feature:ManualPerformance] should be able to handle 3 pods per node'
)

function skipped_test_names () {
    local first=y
    for name in "${TESTS_TO_SKIP[@]}"; do
        if [ -z "${first}" ]; then
            echo -n "|"
        else
            first=
        fi
        echo -n "$(escape_test_name "${name}")\$"
    done
}

if [ -z "${API_SERVER}" ]; then
    echo "Must provide API_SERVER env var" 1>&2
    exit 1
fi

export KUBERNETES_PROVIDER=skeleton
export KUBERNETES_CONFORMANCE_TEST=y

# Configure kube config
cluster/kubectl.sh config set-cluster local --server="${API_SERVER}" --insecure-skip-tls-verify=true
cluster/kubectl.sh config set-context local --cluster=local --user=local
cluster/kubectl.sh config use-context local

if [ -z "${FOCUS}" ]; then
    # non-serial tests can be run in parallel mode
    GINKGO_PARALLEL=y go run hack/e2e.go --v --test -check_version_skew=false \
      --test_args="--ginkgo.focus=\[Conformance\] --ginkgo.skip=\[Serial\]|\[Flaky\]|\[Feature:.+\]|$(skipped_test_names)"

    # serial tests must be run without GINKGO_PARALLEL
    go run hack/e2e.go --v --test -check_version_skew=false --test_args="--ginkgo.focus=\[Serial\].*\[Conformance\] --ginkgo.skip=$(skipped_test_names)"
else
    go run hack/e2e.go --v --test -check_version_skew=false --test_args="--ginkgo.focus=$(escape_test_name "${FOCUS}") --ginkgo.skip=$(skipped_test_names)"
fi