#!/usr/bin/env python

import os
import sys
import string
from glob import glob
from pprint import pprint

def _colorate(string, color = 31, colorate_status = True):
    if not colorate_status:
        return string
    return "\033[1;%dm%s\033[0m" % (color, string)

def _colorate_realname(path, last_color = 32, before_last_color = 36, colorate_status = True):
    if not colorate_status:
        return path
    splitted = path.split('/')
    slash = _colorate('/', 31)
    return slash.join(splitted[:-2] + [_colorate(splitted[-2], before_last_color), _colorate(splitted[-1], last_color)])

def lstree(dir, limit = 1000, ignores = [], indent = False, colorate_status = True):
    dir = os.path.realpath(dir)
    base_depth = dir.count('/')
    for path, dirs, files in os.walk(dir, True):
        current_depth = path.count('/')
        level = current_depth - base_depth + 1
        if indent:
            print "   " * level,
        print "[%s]" % _colorate('D', color = 35, colorate_status = colorate_status),
        print _colorate_realname(path, last_color = 35, colorate_status = colorate_status),
        print
        if level >= limit:
            for dir in dirs:
                dirpath = path + '/' + dir
                if indent:
                    print "   " * level,
                print "[%s]" % _colorate('D', color = 35, colorate_status = colorate_status),
                print _colorate_realname(dirpath, last_color = 35, colorate_status = colorate_status),
                print
                dirs.remove(dir)
        for file in files:
            filepath = path + '/' + file
            if indent:
                print "   " * level,
            print "[%s]" % _colorate('F', color = 31, colorate_status = colorate_status),
            print _colorate_realname(filepath, last_color = 31, colorate_status = colorate_status),
            print "\t\t%d o" % os.path.getsize(filepath),
            print
        for ignore in ignores:
            if ignore in dirs:
                dirs.remove(ignore)


"""
def lstree(dir, limit = 1000, prefix = '', path = ''):
    items = glob('%s/*' % dir)
    #pprint(items)
    for name in items:
        basename = name[len(dir):]
        if name == items[0]:
            newpath = path + '+-' + basename
        else:
            newpath = prefix + '+-' + basename
            if name == items[-1]:
                namprefix = prefix + '   ' + ' ' * len(basename)
            else:
                newprefix = prefix + '|  ' + ' ' * len(basename)
                if glob('%s/*' % name):
                    print(newpath)
                    lstree(name, limit - 1, newprefix, newpath + '-')
                else:
                    print(newpath)
                    """

if __name__ == "__main__":
    for dir in sys.argv[1:]:
        lstree(dir)
