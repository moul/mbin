#!/bin/bash

cat <(brew list) ~/cu/.brew-list | sort -u > /tmp/.brew-list
cp /tmp/.brew-list ~/cu/.brew-list
