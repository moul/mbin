#!/bin/sh

find . -type d -name .svn -prune -o -type f -print0 | xargs -0 grep --color $@
