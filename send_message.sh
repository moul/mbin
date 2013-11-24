#!/bin/sh

#set -x

DEST="$1";
MESSAGE="$2";
IFS=",";

for i in $(echo 'tell application "Messages" to get every service' | osascript); do
    SERVICE_ID=$(echo $i | awk '{ print $3 }');
    echo 'tell application "Messages" \n set theBuddy to buddy "'$DEST'" of service id "'$SERVICE_ID'" \n send "'$MESSAGE'" to theBuddy \nend tell' | osascript > /dev/null
done
echo "It's done baby";
