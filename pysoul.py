#!/usr/bin/env python

import traceback
import netsoul
import socket, time, urllib, os, sys, select, re, datetime
from optparse import OptionParser

__author__ = 'moul'
__version__ = '0.1'

def pysoul_debug(str, type = 'server'):
    print "%s: %s %s" % (datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), type, str.rstrip())

if __name__ == "__main__":
    NS_USERNAME = os.getenv("NS_USERNAME")
    NS_PASSWORD = os.getenv("NS_PASSWORD")
    NS_LOCATION = os.getenv("NS_LOCATION")
    parser = OptionParser(usage = '%prog')
    parser.add_option("-s", "--server", dest = "server_host", action = "store", help = "Netsoul server server", default = "ns-server.epitech.net")
    parser.add_option("-P", "--port", dest = "server_port", action = "store", help = "Netsoul server port", default = 4242, type = "int")
    parser.add_option("-t", "--timeout", dest = "timeout", action = "store", help = "Timeout", default = 1, type = "int")
    parser.add_option("-d", "--debug", dest = "debug", action = "store", help = "Debug level", default = 1, type = "int")
    parser.add_option("-u", "--username", dest = "username", action = "store", help = "Username", default = NS_USERNAME)
    parser.add_option("-p", "--password", dest = "password", action = "store", help = "Password", default = NS_PASSWORD)
    parser.add_option("-l", "--location", dest = "location", action = "store", help = "Location", default = NS_LOCATION)
    parser.add_option("-i", "--ip", dest = "ip", action = "store", help = "Ip", default = None)
    parser.add_option("-a", "--agent", dest = "agent", action = "store", help = "Agent", default = "pysoul")
    parser.add_option("-S", "--status", dest = "status", action = "store", help = "Status", default = "actif")
    parser.add_option("-D", "--daemon", dest = "daemon", action = "store_true", help = "Daemon mode", default = False)
    #parser.add_option("-U", "--unix-socket", dest = "unix_socket", action = "store", help = "Unix socket path", default = "/tmp/pysoul.sock")
    parser.add_option("-U", "--unix-socket", dest = "unix_socket", action = "store", help = "Unix socket path", default = False)
    #parser.add_option("-I", "--inet-socket", dest = "inet_socket", action = "store", help = "Inet socket port listening", default = 4242, type = "int")
    parser.add_option("-I", "--inet-socket", dest = "inet_socket", action = "store", help = "Inet socket port listening", default = False, type = "int")

    (options, args) = parser.parse_args()

    isrep = re.compile('^(rep|user_cmd |exec exec)')
    isextuserlog = re.compile('^ext_user_log\ .*\ .*\ .*\ .*$')

    reconnect_sleep = 3

    if options.daemon:
        print "Daemon mode"
    while True:
        try:
            i = False
            l = False
#            print 3
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(options.timeout)
            print options.server_host + ' ' + str(options.server_port)
            s.connect((options.server_host, options.server_port))
            sf = s.makefile()
            ns = netsoul.ns(socket = s, debug = pysoul_debug)
            try:
                u = False
                location = urllib.quote(options.location) if options.location else '-'
                agent = urllib.quote(options.agent) if options.agent else '-'
                status = urllib.quote(options.status) if options.status else '-'
                ns.connect(username = options.username, password = options.password, location = location, agent = agent, status = status)
                if options.ip:
                    if options.ip != ns.hello['ip']:
                        reconnect_sleep = 0.5
                        raise "bad ip"
                    else:
                        reconnect_sleep = 3
                input = [s, sys.stdin]
                if options.unix_socket:
                    u = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    try:
                        os.remove(options.unix_socket)
                    except OSError:
                        pass
                    u.bind(options.unix_socket)
                    u.listen(1)
                    input.append(u)
                if options.inet_socket:
                    l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    l.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    l.bind(('127.0.0.1', options.inet_socket))
                    l.listen(1)
                    input.append(l)
                running = True
                clients = []
                clients_line_counter = {}
                while running:
#                    print 4
                    inputready = None
                    inputready, outputready, exceptready = select.select(input,[],[], 100)
                    if not inputready:
                        pysoul_debug("> ping", type = "server")
                        s.send('ping\n')
                    for sock in inputready:
#                        print 98
                        if sock == u:
                            try:
                                client, address = u.accept() 
                                pysoul_debug("new local client (socket unix)", type = 'local')
                                client_file = client.makefile()
                                client.send('salut 1988 98ddca8b1806b651a926d035f286aa89 88.175.75.62 54373 1256501258\n')
                                clients.append({'socket': client, 'socket_file': client_file})
                                input.append(client_file)
                            except:
                                pass

                        if sock == l:
                            try:
                                client, address = l.accept() 
                                pysoul_debug("new local client (socket inet)", type = 'local')
                                client_file = client.makefile()
                                client.send('salut 1988 98ddca8b1806b651a926d035f286aa89 88.175.75.62 54373 1256501258\n')
                                clients.append({'socket': client, 'socket_file': client_file})
                                input.append(client_file)
                            except:
                                pass

                        elif sock == s:
                            nb = 0
                            while True:
                                nb += 1
                                data = ''
                                try:
                                    data = sf.readline()
                                    if not len(data):
                                        raise socket.error, (0, "Ns-server is down")
                                    parsed = data.strip()
                                    pysoul_debug('< %s' % data)
                                    for client in clients:
                                        pysoul_debug('> %s' % data, type = 'client')
                                        client['socket'].send(data)
                                    if parsed == 'ping 600':
                                        pysoul_debug('> %s' % data, type = 'server')
                                        s.send(data)
                                        break
                                except socket.timeout:
                                    print "timeout"
                                    break
                                except:
#                                    break
                                    trace = ""
                                    exception = ""
                                    for entry in traceback.format_exception_only(sys.exc_type, sys.exc_value):
                                        exception += entry
                                    for entry in traceback.format_tb(sys.exc_info()[2]):
                                        trace += entry
                                    print "%s\n%s" % (exception, trace)
                                    pass
                                if data == "" and nb == 1:
                                    raise socket.error, (0, "Disconnecting (152353)")
#                                if isrep.match(data):
#                                    break
#                            print 7
#ICI !!

                        elif sock == sys.stdin:
                            data = sys.stdin.readline() 
                            if data == 'reconnect\n':
                                raise socket.error, (0, "Reconnecting")
                            if data == 'help\n':
                                print "- help"
                                print "- reconnect"
                            pysoul_debug('< %s' % data, type = 'stdin')
                            pysoul_debug('> %s' % data, type = 'server')
                            s.send(data)

                        else:
#                            print 41
                            data = ''
                            try:
                                data = sock.readline()
                                fd = sock.fileno()
                                if not fd in clients_line_counter:
                                    clients_line_counter[fd] = 1
                                else:
                                    clients_line_counter[fd] += 1
                                if data:
                                    pysoul_debug('< (%d) %s' % (clients_line_counter[fd], data), type = 'client')
                                    for client in clients:
                                        if client['socket_file'] == sock:
                                            client_socket = client['socket']
                                            break
                                    if (clients_line_counter[fd] == 1 and data == 'auth_ag ext_user none none\n') or (clients_line_counter[fd] == 2 and isextuserlog.match(data)):
                                        d = 'rep 002 -- cmd end\n'
                                        pysoul_debug('> %s' % d, type = 'client')
                                        client_socket.send(d)
                                    else:
                                        pysoul_debug('> %s' % data, type = 'server')
                                        s.send(data)
                                else: 
                                    pysoul_debug('Local client disconnecting', type = 'client')
                                    clients_line_counter[sock.fileno()] = 0
                                    sock.close() 
                                    for client in clients:
                                        if client['socket_file'] == sock:
                                            clients.remove(client)
                                    input.remove(sock)
                            except:
                                trace = ""
                                exception = ""
                                for entry in traceback.format_exception_only(sys.exc_type, sys.exc_value):
                                    exception += entry
                                for entry in traceback.format_tb(sys.exc_info()[2]):
                                    trace += entry
                                print "%s\n%s" % (exception, trace)
                                pass

            except netsoul.nsException:
                pysoul_debug("Connection error: %s" % (sys.exc_value), type = 'server')
                pass
            raise socket.error, (0, "Disconnecting (122412)")
            
#        except socket.error, message:
        except:
            pysoul_debug("Aborting: %s" % (sys.exc_value))
            trace = ""
            exception = ""
            for entry in traceback.format_exception_only(sys.exc_type, sys.exc_value):
                exception += entry
            for entry in traceback.format_tb(sys.exc_info()[2]):
                trace += entry
            print "%s\n%s" % (exception, trace)
            try: s.close() 
            except: pass
            try: f.close() 
            except: pass
            pysoul_debug('Trying to reconnect in:')
            for i in xrange(reconnect_sleep):
                pysoul_debug('%d sec... ' % (reconnect_sleep - i))
                time.sleep(1)
            if reconnect_sleep < 1:
                time.sleep(reconnect_sleep)
            continue

