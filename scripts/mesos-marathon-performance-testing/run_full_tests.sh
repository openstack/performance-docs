#!/bin/bash
DATE=$(date +%Y-%m-%d-%H-%M-%S)
FILE_RESULTS="marathon-mesos-test-results-$DATE"
MARATHON_URL="http://127.0.0.1:8080/marathon"

TOP_DIR=$(cd $(dirname "$0") && pwd)
cd ${TOP_DIR}

virtualenv .venv
VPYTHON=".venv/bin/python"
.venv/bin/pip install -r requirements.txt

echo "[" > ${FILE_RESULTS}.json
for test in create update_cpu update_mem update_disk update_instances restart delete; do
    for concur in 1 2 4 8 16; do
        for nodes in 50 100 500; do
            echo "$(date) - Start test $test with concurrency $concur with $nodes nodes"
            $VPYTHON marathon-scale-tests.py -m $MARATHON_URL -t${test} -c${concur} -n${nodes} -s >> ${FILE_RESULTS}.json
            # If something wrong, clean all
            sleep 30
            $VPYTHON application_managment_helper.py  -m $MARATHON_URL -edelete
        done
    done
done
sed -i '$ s/.$//' ${FILE_RESULTS}.json
echo "]" >> ${FILE_RESULTS}.json
