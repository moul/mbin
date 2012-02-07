#!/bin/sh

ip=$1
nmap -v -Tinsane -sS -P0 -p1-65535 $ip
