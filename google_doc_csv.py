#!/usr/bin/env python

import urllib2, csv, sys

url = sys.argv[1].replace('=html', '=csv')
content = urllib2.urlopen(url).read()
for line in csv.reader(content.split('\n')):
    print ';'.join(line)
