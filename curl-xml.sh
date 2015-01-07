#!/bin/bash

if [ "$1" = "-i" ]; then
    shift
    curl -H "Accept: text/xml" -I -XGET $@
fi

curl -H "Accept: text/xml" -s $@ | xmllint --format -
