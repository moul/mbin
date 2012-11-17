#!/bin/sh

ssh $1 -t "tmux attach $2 -t manfred || (tmux new-session -s manfred; attach)"
