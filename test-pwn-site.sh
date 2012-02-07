#!/bin/sh

#set -x

site=$1

FILE=$HOME/mbin/testpwnsite.txt
if [ ! -f $FILE ]; then
    FILE=$(dirname $0)/testpwnsite.txt
fi
for e in $(cat $FILE); do
    url=$site/$e
    printf "$url\r\t\t\t\t\t\t\t"
    a=$(curl -s -A firefox -X GET -I $url)
    echo "$a" | head -n 1
    echo "$a" | grep -i location
done
