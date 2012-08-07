#!/usr/bin/env python
"""
Reads search terms on stdin and outputs google suggestions on stdout
"""

import subprocess
import shlex
import json
import io
import sys
import os
import fcntl


def escape(string):
    return "%s" %(string.replace('\\', '\\\\')
        .replace(' ', '+')
        .replace('"', '\\"')
        .replace("'", "\\'")
        .replace('$', '\\$')
        .replace('`', '\\`')
        .replace('&', '\\&')
        .replace('&', '\\&'))


def print_suggestions(query):
    args = shlex.split("curl -s http://google.com/complete/search\?q=" +
            query + "\&output=json")
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    output = p.communicate()[0].decode('iso-8859-1')
    clean_output = output[len('window.google.ac.h('):len(output) - 1]
    json_translation = json.load(io.StringIO(clean_output))
    for suggestion in json_translation[1]:
        print(suggestion[0])

if __name__ == "__main__":
    # make stdin a non-blocking file
    #print_suggestions(escape(sys.stdin.readline()))
    while True:
        s = sys.stdin.readline()
        if not s:
            break
        else:
            print_suggestions(escape(s))
