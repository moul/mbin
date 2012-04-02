#!/bin/sh
find . \( -name "*~" -or -name ".??*~" -or -name "*.pyc" -or -name "#*#" -or -name ".#*" -or -name ".DS_Store" -or -name "*@SynoResource" \) -delete
