#!/bin/bash

IMAGE=$1

node \
    ~/Git/moul/node-onlinelabs/examples/create_server.js \
    --bootscript=e9d7a0b8-e58f-49d2-8dc1-f03d660dc40d \
    --snapshot=d436a0a1-36a1-4dbf-9237-0fea957dc970 \
    --tags=boot=rescue \
    --tags=ip=dhcp \
    --tags="rescue_image=http://212.47.225.66/test-images/ocs-$IMAGE.tar" \
    --name="[rescue] $IMAGE" \
    --start
