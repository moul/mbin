#!/bin/bash

URL="$1"

raw=$(curl -s -A firefox -X GET -I "$URL")
echo "$raw" | head -n 1
echo "$raw" | grep -i location
