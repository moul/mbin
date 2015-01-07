#!/bin/bash

if [ "$1" = "-i" ]; then
    shift
    curl -I -XGET $@
fi

curl -H "Accept: application/json" -s $@ | python -m json.tool
