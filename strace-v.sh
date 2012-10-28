#!/bin/sh

strace -s 100000 -e execve -f $@
