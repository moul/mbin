#!/bin/bash

if [ "$1" = "-i" ]; then
    shift
    curl -I -XGET $@
fi

curl -H "Accept: text/xml" -s $@ | xmllint --format -
