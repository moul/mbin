#!/bin/bash

killall iTunes && sleep 10
open -a iTunes;  sleep 10

osascript \
    -e 'tell application "iTunes" to activate' \
    -e   'tell application "System Events"' \
    -e     'tell application process "iTunes"' \
    -e       'click menu item "Update iTunes Match" of menu 1 of menu bar item "Store" of menu bar 1' \
    -e     'end tell' \
    -e   'end tell'
