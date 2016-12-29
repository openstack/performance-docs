#!/bin/bash
ansible-playbook -i ./hosts ./deploy-graf-prom.yaml --tags "grafana"
