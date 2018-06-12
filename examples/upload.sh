#!/bin/sh

## requirements: linux, curl

## modify:
NODE_UUID="f5dba253-c0ea-475e-9f8b-3733168dc42e"
NODE_TOKEN="1e4478a5b0f7d622a5d4e60ee694fc7188c649d5"
##

curl --header "Authorization: Token ${NODE_TOKEN}" \
     -F upload_type=testupload -F upload=@test10.raw \
     http://localhost:8023/api/v1/nodes/${NODE_UUID}/upload/
