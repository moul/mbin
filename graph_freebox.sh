#!/bin/sh

FBOXCOOKIE=/tmp/fbox_cookie
WGETCMD="wget -q --load-cookies $FBOXCOOKIE"
FBOXLOGINURL="http://mafreebox.freebox.fr/login.php?login=freebox&passwd=9rb54xc6"
FBOXRRDURL="http://mafreebox.freebox.fr/rrd.cgi"
DESTDIR="$HOME/Sites/fbx/"
WIDTH=640
HEIGHT=110

$WGETCMD --save-cookies $FBOXCOOKIE -O /dev/null $FBOXLOGINURL

for PERIOD in hour day week; do
    for PORT in 0 1 2 3 4; do
        if [ "$PORT" == 0 ]; then # WAN
            DIRLIST="up down"
            DB="db=fbxconnman"
            NAME="wan"
        else
            DIRLIST="tx rx" #LAN
            DB="db=fbxios&port=$PORT"
            NAME="lan$PORT"
        fi
        for DIR in $DIRLIST; do
            [ "$DIR" == "tx" -o "$DIR" == "up" ] && COLOR=3366CC || COLOR=66CC33
            $WGETCMD -O "$DESTDIR/$NAME-$DIR-$PERIOD.png" "$FBOXRRDURL?$DB&dir=$DIR&w=$WIDTH&h=$HEIGHT&color1=$COLOR&color2=FF9999&period=$PERIOD"
        done
    done
done
