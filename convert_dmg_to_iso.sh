#!/bin/sh

source=$1
dest=$source.iso

hdiutil convert $source -format UDTO -o $dest
