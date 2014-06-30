#!/bin/bash

if [ $# -gt 0 ]; then
    LSOF=$(lsof -i -n -P | grep '>' |  cut -d'>' -f2 | cut -d: -f1 | grep "$1")
else
    LSOF=$(lsof -i -n -P | grep '>' | cut -d'>' -f2 | cut -d: -f1)
fi

echo -n Total:
echo "$LSOF" | wc -l
echo
echo "$LSOF" | sort | uniq -c | sort -n -r
