#!/usr/bin/env coffee

dest = 'free.fr:80'
listenport  = 8080
listenportloop = 8081
directory = '/tmp'

options =
    router:
        "localhost/proxy/":   dest
        "localhost/":         "127.0.0.1:#{listenportloop}"

httpProxy = require 'http-proxy'
httpProxy.createServer(options).listen listenport

connect = require 'connect'
connect.createServer(connect.favicon(), connect.static(directory)).listen listenportloop

console.log "Listening to http://127.0.0.1:#{listenport}"
