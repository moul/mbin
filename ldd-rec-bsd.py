#!/usr/bin/env python2.7

import os
import sys

def ldd(path, processed=None):
    if not processed:
        processed = []
    print(path)
    new_ones = os.popen("ldd %s | sed '1,2d' | awk '{print $7}'" % path).read().split('\n')
    processed.append(path)

    for entry in new_ones:
        if entry in processed:
            continue
        if entry == "":
            continue
        ldd(entry, processed)
    return processed

print('\n'.join(sorted(ldd(sys.argv[1]))))
