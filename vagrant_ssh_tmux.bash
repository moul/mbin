#!/bin/bash

HOST=$1

vagrant halt $HOST
vagrant up $HOST
vagrant ssh $HOST -- -t "sudo -i /bin/bash -c 'tmux a -t manfred || tmux new-session -s manfred || /bin/sh'"
