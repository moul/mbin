#!/bin/sh

while true; do
    mosh $1 -- tmux attach $2 -t manfred
    sleep 2
done

