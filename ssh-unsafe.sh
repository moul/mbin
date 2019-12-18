#!/bin/bash

ssh \
    -q \
    -o ControlMaster=no \
    -o UserKnownHostsFile=/dev/null \
    -o StrictHostKeyChecking=no \
    $@
