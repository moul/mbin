#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import os
from struct import unpack


with open(os.path.expanduser(sys.argv[1]), 'rb') as f:
    data = f.read()

pageSize = unpack('>h', data[16:18])[0]
pageList = []

for offset in range(0, len(data), pageSize):
    if data[offset] == '\x0d':
        pageList.append(offset)

def clean_block(block):
    ret = ''
    for char in block:
        o = ord(char)
        if o < 1:
            ret += '.'
        else:
            ret += char
            #ret += str(o) + ' '
    return ret

for offset in pageList:
    page = data[offset: offset + pageSize]

    pageHeader = unpack('>bhhhb', page[:8])
    pageByte, fbOffset, cellQty, cellOffset, freebytes = pageHeader
    print(pageByte, fbOffset, cellQty, cellOffset, freebytes)

    # get unallocated
    start = 8 + cellQty * 2
    end = cellOffset-start
    unalloc = page[start:end]
    #print(offset, unalloc)

    # get freeblocks, if any
    if fbOffset > 0:
        while fbOffset != 0:
            start, size = unpack('>hh', page[fbOffset: fbOffset + 4])
            print(start, size)
            freeblock = page[fbOffset:fbOffset + size]
            #freeblock = clean_block(freeblock)
            print(offset, freeblock)
            #print(freeblock)
            fbOffset = start
