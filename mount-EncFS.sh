#!/bin/bash

mount_enc() {
  umount "$2"
  password=$(security find-generic-password -ga EncFS 2>&1 >/dev/null | cut -d'"' -f2)
  echo "$password" | /usr/local/bin/encfs -S "$1" "$2"
}

mount_enc_with_passphrase() {
  umount "$2"
  echo "$3" | /usr/local/bin/encfs -S "$1" "$2"
}

# mount_enc                 /path/to/encrypted/directory /path/to/decrypted/directory
# mount_enc_with_passphrase /path/to/encrypted/directory /path/to/decrypted/directory passphrase

if [ "$#" -e 3 ]; then
    mount_enc_with_passphrase $@
fi

if [ "$#" -e 2 ]; then
    mount_enc $@
fi
