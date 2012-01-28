#!/usr/bin/env python

from random import shuffle

#chars = map(chr, range(97, 123)) + range(0, 10)
chars = map(chr, range(65, 91)) + range(0, 10)
shuffle(chars)
lines = 6
columns = 6
for l in xrange(lines):
    for c in xrange(columns):
        print chars[l * columns + c],
    print
