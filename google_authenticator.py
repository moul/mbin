#!/usr/bin/env python
"""
copyright 2011 Tomasz Jaskowski
copyright 2012 Christophe-Marie Duquesne

License: LGPL

Simple script to generate tokens compatible with google_authenticator.
Meant to work everywhere (only builtin dependencies). Modified from
http://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python

Just drop your secret in ~/.google_authenticator, like this:

    [login@gmail.com]
    secret = jbswy3dpehpk3pxp

    [another@yourdomain.tld]
    secret = ozsxe6jam5swk2zb

Getting your secret: https://accounts.google.com/SmsAuthConfig
Then remove/replace, and grab it at QR-code flashing step.

The same can be achieved with http://www.nongnu.org/oath-toolkit/.
    oathtool --totp --base32 jbswy3dpehpk3pxp
    oathtool --totp --base32 ozsxe6jam5swk2zb
"""
#TODO: handle the case when the local clock is out of sync. The android
#app does this by grabbing the date from the http header response of a GET
#request on https://www.google.com. See
#http://code.google.com/p/google-authenticator/source/browse/src/com/google/android/apps/authenticator/timesync/NetworkTimeProvider.java?repo=android

import hmac, base64, struct, hashlib, time, ConfigParser, os.path

def get_hotp_token(key, intervals_no):
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(key):
    return get_hotp_token(key, intervals_no=int(time.time())//30)

def main():
    config = ConfigParser.RawConfigParser()
    config.read(os.path.expanduser('~/cu/.gauth'))
    for section in config.sections():
        try:    secret = config.get(section, 'secret')
        except: secret = None
        try:    key = config.get(section, 'key')
        except: key = None
        try:    hexkey = config.get(section, 'hexkey')
        except: hexkey = None
        if hexkey:
            key = hexkey.decode('hex')
        if secret:
            key = base64.b32decode(secret, casefold = True)
        current = str(get_totp_token(key)).zfill(6)
        next = str(get_hotp_token(key, intervals_no=int(time.time()+30)//30)).zfill(6)
        print '%-36s current=%s, next=%s' % ("%s, " % section, current, next)

    remaining = int(30 - (time.time() % 30))
    print
    print '%s seconds remaining before next loop' % remaining

if __name__ == "__main__":
    main()
