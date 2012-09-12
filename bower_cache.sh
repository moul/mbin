#!/bin/sh

mkdir -p /tmp/components
cd /tmp/components
bower search | awk '{print $2}' | remove_color.pl | sed '2d;$d' | xargs bower install
