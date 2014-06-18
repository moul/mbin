#!/bin/bash

if [ $# -gt 0 ]; then
    ps auxwww | grep "$1" | grep -v grep | awk "{print \$2}" | xargs kill
fi
