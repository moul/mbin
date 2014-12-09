#!/bin/bash

while true; do
    $@
    if [ $? == 0 ]; then
        exit
    fi
    sleep .5
done
