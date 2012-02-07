#!/usr/bin/env python

def md5_file(f, block_size = 2 ** 20):
    from hashlib import md5
    m = md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

if __name__ == "__main__":
    from sys import argv
    f = open(argv[1], 'r')
    print md5_file(f)
