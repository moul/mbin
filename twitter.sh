#!/bin/sh

TMP_FILE=/tmp/twitter.tmp

wget -O $TMP_FILE "http://search.twitter.com/search.json?q=$1&rpp=500"

cat $TMP_FILE | tr "," "\n" | grep '^\"text"' | cut -d"\"" -f4 | tr " " "\n" | sed 's/\"//g;s/^[\#\@]//g' | grep -v http: | grep -v "\\\\"

#rm -f $TMP_FILE

