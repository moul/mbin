#!/usr/bin/env python

import re
import readline

def pretty_hex2bin(input):
    try:
        hex = int(input, 16)
    except:
        return "parse error"
    binary = "{0:020b}".format(hex).zfill(32)
    pretty_binary = re.sub("(.{4})", "\\1|", binary, re.DOTALL).strip('|')
    colored_pretty_binary = pretty_binary.replace('0', '*TMP*').replace('1', '\033[1;32m1\033[0m').replace('*TMP*', '\033[0;33m0\033[0m')
    return "%14s     ->     %s" % (input, colored_pretty_binary)

if __name__ == "__main__":
    from sys import argv
    print '                          0000 0000|0011 1111|1111 2222|2222 2233'
    print '                          0123 4567|8901 2345|6789 0123|4567 8901'
    print '                          ---------+---------+---------+---------'
    print '                          3322 2222|2222 1111|1111 1100|0000 0000'
    print '                          1098 7654|3210 9876|5432 1098|7654 3210'
    print '                          ---------+---------+---------+---------'
    if len(argv) > 1:
        for input in argv[1:]:
            print pretty_hex2bin(input)
    else:
        while True:
            print pretty_hex2bin(raw_input('> '))

