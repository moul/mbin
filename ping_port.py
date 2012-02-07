#!/usr/bin/env python

from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, getservbyport
from time import sleep, time
import sys

def isOpen(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def serviceName(port, proto = 'tcp'):
    try:
        name = getservbyport(port, proto)
        return name
    except:
        return port

if __name__ == "__main__":
    seq = 0
    seq_success = 0
    min_time, max_time, total_time = -1, -1, 0
    hostname, port, proto = sys.argv[1], int(sys.argv[2]), 'tcp'
    ip = gethostbyname(hostname)
    service = serviceName(port, proto)
    print "PING %s (%s) PORT %d (%s) PROTO %s" % (hostname, ip, port, service, proto)
    while True:
        try:
            t = time()
            if isOpen(ip, port):
                diff = time() - t
                if min_time == -1:
                    min_time = diff
                    max_time = diff
                else:
                    min_time = min(min_time, diff)
                    max_time = max(max_time, diff)
                total_time += diff
                print "Connected to %s: seq=%d time=%.2fms protocol=%s port=%d" % (ip, seq, diff * 1000, proto, port)
                seq_success += 1
            else:
                print "Request timeout for seq %d" % seq
            seq += 1
            sleep(1 - (t - time()))
        except (KeyboardInterrupt, SystemExit):
            print
            print "--- %s ping port statistics ---" % hostname
            packet_loss = 100 - (seq / seq_success * 100) if seq_success else 0
            print "%d packets transmitted, %d packets received, %.1f%% packet loss" % (seq, seq_success, packet_loss)
            print "round-trip min/avg/max = %.3f/%.3f/%.3f ms" % (min_time * 1000, total_time / seq * 1000, max_time * 1000)
            sys.exit(0)
