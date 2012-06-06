#!/bin/sh

DEST=/tmp/twitter-words.txt

> $DEST.tmp
for word in military navy sailor boat harbor iraq afganastan afghanistan singles dating love facebook; do
    twitter.sh $word >> $DEST.tmp
done
wc -l $DEST.tmp
sort -u $DEST.tmp > $DEST
wc -l $DEST