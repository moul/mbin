#!/bin/sh

SOURCE="$1"
DESTINATION="$1.decrypted.pdf"
PASSWORD="$2"

gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile="$DESTINATION" -c .setpdfwrite -sPDFPassword="$PASSWORD" -f "$SOURCE"

