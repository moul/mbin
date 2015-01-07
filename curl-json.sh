#!/bin/bash

if [ "$1" = "-i" ]; then
    shift
    curl -H "Accept: application/json" -I -XGET $@
fi

curl -H "Accept: application/json" -s $@ | python -m json.tool
