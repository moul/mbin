#!/bin/bash

URL="$1"

raw=$(curl -s -A firefox -X GET -I "$URL")
echo "$row" | head -n 1
echo "$row" | grep -i location
