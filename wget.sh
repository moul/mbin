#!/bin/sh

BASENAME=$(basename "$1")

curl "$1" > "$BASENAME"
