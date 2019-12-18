#!/bin/sh

if [ -z "$SLEEP" ]; then
    SLEEP=.5
fi

command="$@"
while true; do
    a=$(/bin/sh -c "$command" 2>&1)
    clear
    date
    echo
    echo "$command"
    echo
    echo "$a"
    sleep "$SLEEP"
done
