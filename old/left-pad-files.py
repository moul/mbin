#!/usr/bin/env python

import sys, shutil

pad_length = int(sys.argv[1])
pad_char = sys.argv[2]
files = sys.argv[3:]

#print pad_length, pad_char, files
for file in files:
    newname = file.rjust(pad_length, pad_char)
    #newname = file.zfill(pad_length)
    if file != newname:
        print 'moving %s -> %s' % (file, newname)
        shutil.move(file, newname)
