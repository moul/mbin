#!/bin/bash

if [ $# -gt 0 ]; then
    LSOF=$(lsof -i -n -P | grep "$1")
else
    LSOF=$(lsof -i -n -P)
fi

echo -n Total:
echo "$LSOF" | wc -l
echo
echo "$LSOF" | awk "{print \$2}" | sort | uniq -c | sort -n -r
