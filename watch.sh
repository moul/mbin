#!/bin/sh

command=$@
while true; do
    a=$($command 2>&1)
    clear
    date
    echo
    echo $command
    echo
    echo "$a"
    sleep .5
done
