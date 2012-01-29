#!/usr/bin/env python

import sys, urllib2, urllib, re

class rapidshare_folder_extracter():
    def __init__(self, url):
        self.url = url

    def get_links(self):
        req = urllib2.Request(self.url)
        response = urllib2.urlopen(req)
        html = response.read()
        links = []
        for m in re.finditer('<a href="(http://[^"]*)" target="_blank">Start download</a>', html):
            links.append(m.group(1))
        return links

if __name__ == "__main__":
    print '\n'.join(rapidshare_folder_extracter(sys.argv[1]).get_links())
