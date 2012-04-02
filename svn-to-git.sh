#!/bin/sh

REPOS_URL=$1

svn log $REPOS_URL -q | awk -F '|' '/^r/ {sub("^ ", "", $2) sub(" $", "", $2); print $2" = "$2" <"$2"@42.am>"}' | sort -u > authors-transform.txt
git svn clone $REPOS_URL -A authors-transform.txt
