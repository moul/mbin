#!/bin/bash

ssh \
    -o ControlMaster=no \
    -o UserKnownHostsFile=/dev/null \
    -o StrictHostKeyChecking=no \
    $@
