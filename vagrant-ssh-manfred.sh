#!/bin/sh

vagrant ssh -- -t 'tmux a -t manfred || tmux new-session -s manfred'
