#!/bin/sh

ssh $1 -t "tmux attach $2 -t corentin || tmux new-session -s corentin"
