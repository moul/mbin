#!/bin/sh
find . -type l | (while read -r FN ; do test -e "$FN" || ls -ld "$FN"; done)
