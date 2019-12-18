#!/bin/sh

# Checks if there's a frame open
emacsclient -n -e "(if (> (length (frame-list)) 1) 't)" 2>/dev/null | grep t &>/dev/null

ARGS="$@"
if [ "$ARGS" = "" ]; then
    ARGS="."
fi

if [ "$?" -eq "1" ]; then
    emacsclient -a '' -nw $ARGS
else
    emacsclient -nw $ARGS
fi
