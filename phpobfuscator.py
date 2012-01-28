#!/usr/bin/env python

import re
import base64
import random
import operator
from encodings.rot_13 import rot13
from StringIO import StringIO

class phpObfuscator:
    _functions = {}

    def __init__(self, payload = None):
        self._payload = payload

    def set_payload(self, payload):
        self._payload = payload
        return self

    def _get_rand_string(self, length = 6):
        string = ''
        for i in xrange(length):
            string += chr(random.randrange(97, 122))
        return string

    def rot13(self, string):
        outfile = StringIO()
        rot13(StringIO(string), outfile)
        return outfile.getvalue()

    def xor(self, string, key):
        string_l = len(string)
        key_l = len(key)
        xored_string = ''
        for i in xrange(string_l):
            xored_string += chr(operator.xor(ord(string[i]), ord(key[i % key_l])))
        return xored_string

    def _alias_function(self, function, alias = None):
        if alias is None:
            alias = self._get_rand_string(2)
            while alias in self._functions:
                alias = self._get_rand_string(2)
        self._functions[alias] = function

    def _alias_function_init(self):
        init = ''
        for alias, function in self._functions.items():
            init += '$%s=\'%s\';' % (alias, function)
        return init

    def _alias_function_alter(self, string):
        for alias, function in self._functions.items():
            string = string.replace('%s(' % function, '$%s(' % alias)
        return string

    def obfuscate(self, recursive = 3):
        payload = self._payload
        if payload[0:5] == '<?php':
            payload = payload[5:]
        if payload[0:2] == '<?':
            payload = payload[2:]
        if payload[-5:] == '?>':
            payload = payload[:-5]
        payload = payload.strip()

        if payload.replace('RANDME', '{RANDME}') != payload:
            payload = payload.replace('RANDME', self._get_rand_string())

        payload = re.sub(r'\s*/\*\s*\*/', ' ', payload)
        payload = re.sub(r'//.*', '', payload)
        payload = re.sub('\s+', ' ', payload)

        self._alias_function('base64_decode');
        self._alias_function('ord');
        self._alias_function('chr');
        self._alias_function('str_rot13');
        self._alias_function('print_r');
        self._alias_function('get_defined_vars');
        self._alias_function('set_error_handler');

        xor_key = self._get_rand_string(12)
        payload = self.xor(payload, xor_key)
        payload_len = len(payload)
        payload = base64.b64encode(payload)
        payload = self.rot13(payload)
        payload = '$p=@base64_decode(@str_rot13(\'%s\'));$k=\'%s\';for($i=0;$i<%d;$i++){$p[$i]=chr(ord($p[$i])^ord($k[$i%%%d]));}@eval($p);' % (payload, xor_key, payload_len, len(xor_key))
        payload = self._alias_function_alter(payload)
        payload = self._alias_function_init() + payload
        for i in xrange(recursive):
            payload = '@eval(@base64_decode("%s"));' % (base64.b64encode(payload))
        payload = '<?php %s' % payload

        return payload

if __name__ == "__main__":
    import sys
    payload = open(sys.argv[1]).read()
    recursive = 3
    print phpObfuscator().set_payload(payload).obfuscate(recursive = 3)


