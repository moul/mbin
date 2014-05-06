#!/bin/bash

TARGET=$1
shift
COMMAND="$@"

eval "$COMMAND"
fswatch "$TARGET" "$COMMAND"
