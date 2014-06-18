#!/bin/bash

if [ $# -gt 0 ]; then
    lsof -i -n -P | cut -d'>' -f2 | grep "$1" | cut -d: -f1 | sort | uniq -c | sort -n -r
else
    lsof -i -n -P | cut -d'>' -f2 | cut -d: -f1 | sort | uniq -c | sort -n -r
fi
