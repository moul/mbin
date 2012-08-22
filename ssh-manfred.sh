#!/bin/sh

ssh $1 'tmux a -t manfred || (tmux new-session -s manfred; attach)'
