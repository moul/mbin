#!/bin/bash

ssh_options=""
ssh_options="$ssh_options -o ControlMaster=no"
ssh_options="$ssh_options -o UserKnownHostsFile=/dev/null"
ssh_options="$ssh_options -o StrictHostKeyChecking=no"

mosh -ssh="ssh $ssh_options" -- $@
