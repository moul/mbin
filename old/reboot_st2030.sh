#!/bin/bash

WAIT="5"
username="administrator"
password="784518"

function th2030_reboot
{
    # Thomson ST2030 IP
    IP="$1"

    WGET="wget -q"
    COOKIES=`mktemp`
    ADMIN=`mktemp`

    # Get "seed" for login
    # <input type="hidden" name="nonce" value="c0a800010000058e">
    $WGET --save-cookies $COOKIES --keep-session-cookies "http://$IP/admin.html" -O $ADMIN
    nonce=`grep -m1 'name="nonce"' < $ADMIN | sed 's/^.*value="\(.*\)".*$/\1/'`

    WGET="wget -q --load-cookies $COOKIES -O -"

    # encoded = username + ":" + md5(username + ":" + password + ":" + "c0a8000100000330");
    md5=`echo -n "$username:784518:$nonce" | md5sum | head -c32`
    encoded="$username:$md5"
    post="encoded=$encoded&nonce=$nonce&URL=%2F&goto=Log+On"

    # Login
    $WGET "http://$IP/admin.html" --post-data "$post" &> /dev/null

    # Reboot
    $WGET --read-timeout $WAIT -t 1 "http://$IP/reboot.html" --post-data "" &> /dev/null

    rm -f "$COOKIES" "$ADMIN"
}

for i in $*; do
    echo "reboot $i"
    th2030_reboot $i &
done
