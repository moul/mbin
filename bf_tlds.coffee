#!/usr/bin/env coffee

whois = require('whoisjs').whois
who = new whois

server = require('whoisjs/lib/whois/server').serverdef

tlds = server.tlds()

basedomain = process.argv[2]

checkDomain = (tld) ->
    full = "#{basedomain}#{tld}"
    who.query full, (response) ->
        if response.error()
            setTimeout (-> checkDomain full), 1000
        else
            if response.available()
                console.log "#{full}: #{if response.available() then 'AVAILABLE' else ''} | #{if response.error() then 'ERROR' else ''}"

for tld in tlds
    checkDomain tld
