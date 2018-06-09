#!/bin/sh

## requirements: linux, curl

## modify:
NODE_UUID="f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN="1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
##

DT_UTC=`date -u -Ins | tr "," "."`
curl --url "http://localhost:8023/api/v1/nodes/${NODE_UUID}/status/" \
     --header "Authorization: Token ${NODE_TOKEN}" \
     --header "Content-Type: application/json" \
     --data "{\"status_code\": \"OK\", \"node_time_utc\": \"${DT_UTC}\", \"data\": {\"load\": \"`cat /proc/loadavg | cut -d ' ' -f1`\", \"cpu_count\": `grep processor /proc/cpuinfo | wc -l`}}"
