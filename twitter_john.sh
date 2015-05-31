#!/bin/sh

WORDLIST="$1"
HASHLIST="$2"

/usr/bin/john --wordlist="$WORDLIST" --rules --format=raw-md5 "$HASHLIST"
