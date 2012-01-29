#!/bin/sh

i=1
prefix=1234

###

replace="$prefix"1
while True; do
    URL=$(echo $1 | sed 's/EXPLOIT/'$replace'/')
    echo $URL
    curl -s -i $URL | grep --color -E "$prefix|HTTP"
    i=$(echo $i + 1 | bc)
    replace="$replace+$prefix$i"
    sleep .1
done