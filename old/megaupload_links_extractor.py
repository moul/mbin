#!/usr/bin/env python

import sys, urllib2, urllib, re

class megaupload_links_extracter():
    def __init__(self, hash):
        self.hash = hash
        self.links = []

    def _get_links(self, html):
        for m in re.finditer('(www.megaupload.com/\?d=........)', html):
            self.links.append('http://%s' % m.group(1))

    def get_links(self):
        response = urllib2.urlopen(sys.argv[1])
        html = response.read()
        for m in re.finditer('([a-zA-Z0-9]*\.linkbucks.com)', html):
            print m.group(0)
            try:
                self._get_links(urllib2.urlopen('http://%s/' % m.group(1)).read())
            except:
                pass
        self._get_links(html)
        return unique(self.links)

def unique(inlist, keepstr=True):
    typ = type(inlist)
    if not typ == list:
        inlist = list(inlist)
    i = 0
    while i < len(inlist):
        try:
            del inlist[inlist.index(inlist[i], i + 1)]
        except:
            i += 1
    if not typ in (str, unicode):
        inlist = typ(inlist)
    else:
        if keepstr:
            inlist = ''.join(inlist)
    return inlist

if __name__ == "__main__":
    print '\n'.join(megaupload_links_extracter(sys.argv[1]).get_links())
