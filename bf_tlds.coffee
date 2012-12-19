#!/usr/bin/env coffee

console.log = ->

util = require 'util'
whois = require('whoisjs').whois
server = require('whoisjs/lib/whois/server').serverdef

who = new whois
tlds = server.tlds()
basedomain = process.argv[2]


checkDomain = (tld, retry = 2) ->
    full = "#{basedomain}#{tld}"
    if retry == -1
        util.log "#{full} error"
        return
    who.query full, (response) ->
        if response.error()
            setTimeout (-> checkDomain tld, retry - 1), 1000
        else
            if response.available()
                util.log "#{full} is AVAILABLE"

for tld in tlds
    checkDomain tld
