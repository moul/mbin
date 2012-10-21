#!/bin/sh

ssh $@ -t 'tmux a -t manfred || (tmux new-session -s manfred; attach)'
