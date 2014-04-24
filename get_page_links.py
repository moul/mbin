#!/usr/bin/env python

import sys

from urlparse import urljoin
import requests
from BeautifulSoup import BeautifulSoup, SoupStrainer


def get_page_links(url):
    req = requests.get(url)
    response = req.text

    links = {}
    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        href = link.get('href')
        if not href:
            continue
        full_url = urljoin(url, href)
        if full_url[-1] == '/':
            kind = 'directory'
        else:
            kind = 'file'
        if not kind in links:
            links[kind] = []
        links[kind].append(full_url)
    return links


def main():
    links = get_page_links(sys.argv[1])
    for kind, urls in links.items():
        print(kind)
        print('=' * len(kind))
        for url in urls:
            print('{}'.format(url))
        print('')


if __name__ == '__main__':
    main()
