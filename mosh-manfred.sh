#!/bin/sh

while true; do
    mosh "$1" -- /bin/sh -c 'tmux attach -t manfred $@ || tmux new-session -s manfred || /bin/sh'
    echo "reconnecting to $1 in 5 secs"
    sleep 5
done
