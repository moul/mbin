#!/usr/bin/env python

import re
import readline
import atexit

def color_binary(binary):
    return binary.replace('0', '*TMP*').replace('1', '\033[1;32m1\033[0m').replace('*TMP*', '\033[0;33m0\033[0m')

def group_binary(binary):
    return re.sub("(.{4})", "\\1|", binary, re.DOTALL).strip('|')

def pretty_hex2bin(input):
    if not len(input.strip()):
        return
    input = input.split()
    number = input[0]
    bitsets = input[1:]
    try:
        _hex = int(number, 16)
    except:
        return "parse error"
    binary = "{0:020b}".format(_hex).zfill(32)
    pretty_binary = group_binary(binary)
    colored_pretty_binary = color_binary(pretty_binary)
    out = "\033[1;31m%14s\033[0m          ->           %s\n" % (number, colored_pretty_binary)
    for bitset in bitsets:
        if ':' in bitset:
            bitset_numbers = map(int, bitset.split(':'))
        else:
            bitset_numbers = [int(bitset), int(bitset)]
        bitset_binary = binary[32 - max(bitset_numbers) - 1:32 - min(bitset_numbers)]
        padded_bitset_binary = '.' * (32 - max(bitset_numbers) - 1) + bitset_binary + '.' * (min(bitset_numbers))
        pretty_padded_bitset_binary = group_binary(padded_bitset_binary)
        colored_bitset_binary = color_binary(pretty_padded_bitset_binary)
        bitset_value = int(bitset_binary, 2)
        out += '       \033[1;34m%7s\033[0m    %-5s   %-8s   %s\n' % ('[%s]' % bitset, bitset_value, hex(bitset_value), colored_bitset_binary)
    return out

def print_header():
    print '                                     0000 0000|0011 1111|1111 2222|2222 2233'
    print '                                     0123 4567|8901 2345|6789 0123|4567 8901'
    print '                                     ---------+---------+---------+---------'
    print '                                     3322 2222|2222 1111|1111 1100|0000 0000'
    print '                                     1098 7654|3210 9876|5432 1098|7654 3210'
    print '                                     ---------+---------+---------+---------'

if __name__ == "__main__":
    histfile = './.pb_history'
    try:
        readline.read_history_file(histfile)
    except:
        pass
    atexit.register(readline.write_history_file, histfile)
    del readline, histfile

    from sys import argv
    print_header()
    if len(argv) > 1:
        for input in argv[1:]:
            out = pretty_hex2bin(input)
            if out:
                print out,
    else:
        while True:
            out = pretty_hex2bin(raw_input('> '))
            if out:
                print out

