#!/bin/bash

LIMIT=$1
shift

x=1
while [ $x -le $LIMIT ]
do
    $@
    x=$(( $x + 1 ))
    sleep .05
done
