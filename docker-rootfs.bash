#!/bin/bash

set -e

IMAGE=$1
FLATTEN_IMAGE=flatten

# Create an unmodified container from an image
docker run --entrypoint /IDONTEXISTS$RAND $IMAGE 2>/dev/null || true
container_id=$(docker ps -lq)

# Create a flatten image from the container
docker export $container_id | docker import - $FLATTEN_IMAGE >/dev/null

# Export rootfs as a tarball
docker save $FLATTEN_IMAGE | tar -O -xf - '*/layer.tar'
