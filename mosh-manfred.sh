#!/bin/sh

while true; do
    mosh $1 -- tmux attach $2 -t manfred
    echo "reconnecting to $2 in 2 secs"
    sleep 2
done

