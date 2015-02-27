#!/bin/bash

URL=$1

echo | openssl s_client -connect $URL 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'
