#!/usr/bin/env python

import os
import sys
import readline
import atexit

#import ns_who

if __name__ == '__main__':
    history_file = os.path.join(os.environ['HOME'], '.ns_who_sh_history')
    try:
        readline.read_history_file(history_file)
    except IOError:
        pass
    atexit.register(readline.write_history_file, history_file)

    if len(sys.argv) > 1:
        os.system('clear')
        os.system('ns_who %s' % ' '.join(sys.argv[1:]))
    while True:
        cmd = raw_input('ns_who# ')
        os.system('clear')
        os.system('ns_who %s' % cmd)
