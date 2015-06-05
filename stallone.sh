#!/bin/bash

set -xe

WORD="$1"
FILENAME=$(echo "$WORD" | sed 's/[^a-zA-Z0-9]/-/g')
VOICE=${VOICE:-Stallone}
TEXT=$(echo "$WORD" | perl -p -e 's/([^A-Za-z0-9])/sprintf("%%%02X", ord($1))/seg')
URL="http://voxygen.fr/sites/all/modules/voxygen_voices/assets/proxy/index.php?method=redirect&text=$TEXT&voice=$VOICE&ts=1418550077284"

wget -O "$FILENAME.mp3" "$URL"
afplay "$FILENAME.mp3"
