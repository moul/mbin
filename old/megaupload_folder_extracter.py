#!/usr/bin/env python

import sys, urllib2, urllib, re

extract_url = 'http://tools.half-moon.org/megaupload/'
base_url = 'http://www.megaupload.com/?f='

class megaupload_folder_extracter():
    def __init__(self, hash):
        self.hash = hash

    def get_links(self):
        values = {'url': '%s%s' % (base_url, self.hash)}
        data = urllib.urlencode(values)
        req = urllib2.Request(extract_url, data)
        response = urllib2.urlopen(req)
        html = response.read()
        links = []
        for m in re.finditer('<td><a href="(http://[^"]*)">', html):
            links.append(m.group(1))
        return links

if __name__ == "__main__":
    print '\n'.join(megaupload_folder_extracter(sys.argv[1]).get_links())
