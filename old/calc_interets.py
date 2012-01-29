#!/usr/bin/env python

#futurama: 1000$ 3% 1000 year: ./calc_interets.py 1000 1.03 1000

import sys

base = float(sys.argv[1])
interet = float(sys.argv[2])
limit = int(sys.argv[3])

for i in xrange(1, limit):
    before = base
    after = base * interet
    print "An: %4d, before: %-5f, %-5f, %-5f" % (i, before, after, interet)
    base = after
