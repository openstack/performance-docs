rally  --plugin-paths /home/rally/plugins task start \
keystone.json \
--task-args '{"gre_enabled": true, "compute": 375, "concurrency": 5}' \
--out=keystone.html

rally  --plugin-paths /home/rally/plugins task start \
boot_attach_live_migrate_and_delete_server_with_secgroups.json \
--task-args '{"gre_enabled": true, "compute": 375, "concurrency": 5}' \
--out=boot_attach_live_migrate_and_delete_server_with_secgroups.html

rally  --plugin-paths /home/rally/plugins task start \
create-and-delete-image.json \
--task-args '{"gre_enabled": true, "compute": 375, "concurrency": 5, "http_server_with_glance_images": "1.2.3.4"}' \
--out=create-and-delete-image.html
