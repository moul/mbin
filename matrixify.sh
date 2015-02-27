#!/bin/bash

WIDTH=${WIDTH:-$(stty size 2>/dev/null | awk '{print $2}' | grep -o . || echo 80)}
CHARS=${CHARS:-$(echo "1234567890!@#\$%^&()!@#\$%^&()abcdefghijklmnopqrstuvwxyz,./;'[]\\\`~{}:" | grep -o .)}

# FIXME: make it dynamic
spaces=$(printf "%${WIDTH}s" " ")


random_chars () {
    for i in $CHARS; do
        echo "$RANDOM .$i "
    done \
        | sort -rn \
        | awk '{print $2}' \
        | sed 's/\./ /g' \
        | tr "\n" " " \
        | tr -d ' '
}


while read line; do
    line_width=$(echo "$line" | wc -c)
    if [ $line_width -lt $WIDTH ]; then
        line="$line ${spaces:0:$WIDTH-$line_width}"
    fi

    IFS=
    line_chars=$(echo $CHARS | gshuf | tr "\n" " " | tr -d ' ')
    i=0
    echo "$line" | \
        while read -r -n1 char; do
            if [ "$char" = ' ' ]; then
                if (( ! ( RANDOM % 10 ) )); then
                    printf "\033[0;32m%s\033[0m" "${line_chars:$i:1}"
                else
                    echo -n ' '
                fi
                i=$((i+1))
            else
                printf "\033[1;32m$char\033[0m"
            fi
        done
    echo
done
