#!/bin/bash

retry.bash ssh-unsafe.sh "$1" -t "tmux attach $2 -t manfred || tmux new-session -s manfred || /bin/sh"
