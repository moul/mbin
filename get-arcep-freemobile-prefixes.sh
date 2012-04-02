#!/bin/sh

FILE=/tmp/arcep-freemobile

if [ ! -f $FILE ]; then
    wget 'http://www.arcep.fr/fileadmin/wopnum.xls' -q -O $FILE
fi
xls2csv $FILE | grep FRMO | grep \"06 | cut -d '"' -f 2
