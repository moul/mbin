#!/usr/bin/env python

import netsoul
import socket, urllib, datetime, os
from time import time
from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--server", dest = "server_host", action = "store", help = "Netsoul server server", default = "ns-server.epitech.eu")
    parser.add_option("-P", "--port", dest = "server_port", action = "store", help = "Netsoul server port", default = 4242)
    parser.add_option("-t", "--timeout", dest = "timeout", action = "store", help = "Timeout", default = 3)
    parser.add_option("-u", "--username", dest = "username", action = "store", help = "Username", default = os.getenv('NS_USERNAME'))
    parser.add_option("-p", "--password", dest = "password", action = "store", help = "Password", default = os.getenv('NS_PASSWORD'))
    parser.add_option("-l", "--location", dest = "location", action = "store", help = "Location", default = os.getenv('NS_LOCATION'))
    parser.add_option("-a", "--agent", dest = "agent", action = "store", help = "Agent", default = "pysoul")

    (options, args) = parser.parse_args()

    if len(args) >= 1:
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.connect('/tmp/pysoul.sock')
            s.send("%s\n" % args[0])
        except socket.error, (value, message): 
            print "Could not open socket: " + message 
        except IOError, e:
            if e.errno == errno.EPIPE:
                # EPIPE error
                pass
            else:
                # Other error
                pass
    else:
        print "usage"
