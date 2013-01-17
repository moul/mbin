#!/bin/sh

# from: http://alias.sh/show-lines-are-not-blank-or-commented-out

grep -v -e "^$" -e"^ *#"
