#!/bin/sh

for socket in $(find ~/tmp/.ssh/cm/ -type s); do
    ssh -o ControlPath=$socket -O check 127.0.0.1 2>/dev/null || rm -fv $socket
done
