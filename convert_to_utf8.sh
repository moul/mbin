#!/bin/sh

FROM=iso-8859-1
TO=UTF-8

cp $1 /tmp/convert_to_utf8.tmp
iconv -f $FROM -t $TO < /tmp/convert_to_utf8.tmp > $1
