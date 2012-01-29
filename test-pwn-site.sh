#!/bin/sh

#set -x

site=$1

for e in $(cat $(dirname $0)/testpwnsite.txt); do
    url=$site/$e
    printf "$url\r\t\t\t\t\t\t\t"
    a=$(curl -s -A firefox -X GET -I $url)
    echo "$a" | head -n 1
    echo "$a" | grep -i location
done