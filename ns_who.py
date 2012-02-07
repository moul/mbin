#!/usr/bin/env python

#TODO: KRB5

import netsoul
import socket, urllib, datetime, sys, os, errno
from time import time
from optparse import OptionParser

try:
    import ipaddr
    file_path = os.path.join(os.path.dirname(sys.argv[0]), 'ns.locations')
    ipaddr_entries = []
    for entry in [line.split() for line in file(file_path, 'r+')]:
        ipaddr_entries.append({'ipstr': entry[0], 'range': ipaddr.IPNetwork(entry[0]), 'name': entry[1]})
    ipaddr_enabled = True
except:
    ipaddr_enabled = False

def _get_location_name(ipstr):
    if not ipaddr_enabled:
        return 'n/a'
    try:
#    if 1:
        ipobj = ipaddr.IPAddress(ipstr)
        locations = []
        for entry in ipaddr_entries:
            if ipobj in entry['range']:
                locations.append(entry['name'])
        if len(locations) == 0:
            return 'Unknown'
        return ','.join(locations)
    except:
        return 'Error'

def ns_who_debug(str):
    print str

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--server", dest = "server_host", action = "store", help = "Netsoul server server", default = "ns-server.epitech.net")
    parser.add_option("-P", "--port", dest = "server_port", action = "store", help = "Netsoul server port", default = 4242)
    parser.add_option("-t", "--timeout", dest = "timeout", action = "store", help = "Timeout", default = 2)
    parser.add_option("-d", "--debug", dest = "debug", action = "store", help = "Debug level", default = 0)
    parser.add_option("-g", "--group", dest = "group", action = "store", help = "Group (see ns.listes)", default = None)
    parser.add_option("-r", "--raw", dest = "raw", action = "store_true", help = "Raw line", default = False)
    parser.add_option("-l", "--try-local", dest = "try_local", action = "store_true", help = "Try local socket", default = False)

    (options, args) = parser.parse_args()

    if options.group:
        groups = {}
        file_path = os.path.join(os.path.dirname(sys.argv[0]), 'ns.listes')
        for line in open(file_path, 'r+'):
            lst = line.strip().split()
            groups[lst[0]] = lst[1:]

        for key in groups:
            done = True
            while done:
                done = False
                for login in groups[key]:
                    if login[0] == '@':
                        done = True
                        groups[key] += groups[login[1:]]
                        groups[key].remove(login)

    t = time()

    s = None
    if options.try_local:
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.connect('/tmp/pysoul.sock')
        except:
            pass
    if not s:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(options.timeout)
            s.connect((options.server_host, int(options.server_port)))
        except Exception, e:
            print "OHNOEWS %s" % e
    if s:
        ns = netsoul.ns(s, debug = None)
        list = None
        if args:
            list = args[0]
        users = ns.list_users_iter(list)
        try:
            total = 0
            for user in users:
                if not options.group or user['login'] in groups[options.group]:
                    total += 1
                    if options.raw:
                        print user['raw']
                    else:
                        # $6: niveau e confiance de l'auth: 1 = interne, 3 = externe, 100 = interne + krb
                        if 0:
                            print user['agent']
                        else:
                            print "%-5d %-40s %-17s %-10s %-15s %-30s %-30s" % (user['port'],
                                                                                (user['login'] + '@' + urllib.unquote(user['location']))[:40],
                                                                                user['ip'],
                                                                                _get_location_name(user['ip']),
                                                                                user['group'],
                                                                                (user['status_type'] + ' ' + str(datetime.timedelta(seconds = int(t) - user['status_time']))),
                                                                                urllib.unquote(user['agent'])[:30])
            print "Total: %d" % (total)
        except IOError, e:
            if e.errno == errno.EPIPE:
                # EPIPE error
                sys.exit(0)
            else:
                # Other error
                pass
