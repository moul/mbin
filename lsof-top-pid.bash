#!/bin/bash

if [ $# -gt 0 ]; then
    lsof -i -n -P | grep "$1" | awk "{print \$2}" | sort | uniq -c | sort -n -r
else
    lsof -i -n -P | awk "{print \$2}" | sort | uniq -c | sort -n -r
fi
