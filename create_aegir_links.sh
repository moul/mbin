#!/bin/sh

for e in /data/disk/o*/distro/*/*/sites/*; do
    ln -s $(readlink -f $e) . 2>/dev/null
done
rm all default *.php *~
