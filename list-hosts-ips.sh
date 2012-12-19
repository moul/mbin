#!/bin/sh

sed 's/^\([0-9\.]*\).*$/\1/g;/^$/d' /etc/hosts | sort
