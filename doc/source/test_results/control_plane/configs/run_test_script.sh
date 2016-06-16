${WORK_DIR:?}
DEPLOYMENT_NAME="$(uuidgen)"
DEPLOYMENT_CONFIG="${WORK_DIR}/deployment.json"
PLUGIN_PATH="${WORK_DIR}/plugins/nova_scale.py"
JOB_PARAMS_CONFIG="${WORK_DIR}/job-params.yaml"
rally deployment create --filename $(DEPLOYMENT_CONFIG) --name $(DEPLOYMENT_NAME)
SCENARIOS="boot_attach_live_migrate_and_delete_server_with_secgroups create-and-delete-image keystone.json"
for scenario in SCENARIOS; do
rally --plugin-paths ${PLUGINS_PATH} task start --tag ${scenario} --task-args-file ${JOB_PARAMS_CONFIG} ${WORK_DR}/scenarios/${scenario}
done
task_list="$(rally task list --uuids-only)"
rally task report --tasks ${task_list} --out=${WORK_DIR}/rally_report.html