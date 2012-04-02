#!/bin/sh
echo Int:
ifconfig | grep inet | awk '{print $2}'
echo Ext:
curl ip.anjunabeats.com
