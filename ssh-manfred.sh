#!/bin/sh

ssh $1 -t 'tmux a -t manfred || (tmux new-session -s manfred; attach)'
