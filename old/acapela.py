#!/usr/bin/env python

import urllib, httplib, sys, urlparse, hashlib

def acapela(text, voice = 'claire22k'):
    url = 'http://www.acapela-group.com/Flash/Demo_Web_AS3/demo_web.swf?path=http://vaas.acapela-group.com/Services/DemoWeb/&lang=EN'
    parsed_url = urlparse.urlparse(url)
    post = {'client_request_type': 'CREATE_REQUEST',
            'client_voice': voice,
            'actionscript_compress': 'NO',
            'actionscript_version': 3,
            'client_text': text,
            'client_version': '1-00',
            'client_login': 'asTTS',
            'client_password': 'demo_web'}
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'accept': 'text/plain',
               'referer': 'http://www.acapela-group.com/Flash/Demo_Web_AS3/demo_web.swf?path=http://vaas.acapela-group.com/Services/DemoWeb/&lang=EN',
               }
    conn = httplib.HTTPConnection('%s:%s' % (parsed_url.netloc, 80))

    path = urlparse.urlunparse((None, None, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
    conn.request('POST', path, urllib.urlencode(post), headers)
    response = conn.getresponse()
    #print response.read()
    hash = hashlib.md5('%s-%s' % (voice, text)).hexdigest()
    if response.status == 200:
        open('%s.mp3' % hash, 'w').write(response.read())
        print '[+] %s.mp3 has been created in your current directory !' % hash
    else:
        print "[-] Error"

if __name__ == "__main__":
    acapela(' '.join(sys.argv[1:]))
