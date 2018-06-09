#!/bin/sh

## requirements: linux, curl

## modify:
NODE_UUID="f5dba253-c0ea-475e-9f8b-3733168dc42e"

##

DT_UTC=`date -u -Ins | tr "," "."`
curl --url "http://localhost:8023/api/v1/nodes/${NODE_UUID}/status/" \
     --header 'Content-Type: application/json' \
     --data "{\"status_code\": \"OK\", \"node_time_utc\": \"${DT_UTC}\", \"data\": {\"load\": \"`cat /proc/loadavg`\", \"cpu_count\": `grep processor /proc/cpuinfo | wc -l`}}"
