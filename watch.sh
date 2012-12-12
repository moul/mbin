#!/bin/sh

command=$@
while true; do a=$($command); clear; date;echo; echo $command;echo;echo "$a" ;sleep .5; done
