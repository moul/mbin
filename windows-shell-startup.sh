#!/bin/sh

cd ~

# create new session if not already exists
tmux new-session -s manfred -d || true

# attach to session (detach potentially already connected clients)
exec tmux attach -d -t manfred
