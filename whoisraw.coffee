#!/usr/bin/env coffee

whois = require('whoisjs').whois
who = new whois

domain = process.argv[2]

who.query domain, (response) ->
    console.dir response
    console.log response.raw
    info =
        available:   do response.available
        error:       do response.error
        unavailable: do response.unavailable
        timeout:     do response.timeout
    info.state = "available"   if info.available
    info.state = "unavailable" if info.unavailable
    info.state = "timeout"     if info.timeout
    info.state = "error"       if info.error
    info.state ||= "unknown"
    console.dir info