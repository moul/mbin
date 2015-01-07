#!/bin/bash

if [ "$1" = "-i" ]; then
    shift
    curl -I -XGET $@
fi

curl -s $@ | python -m json.tool
