#!/usr/bin/env coffee

fs = require 'fs'
sys = require 'sys'
whois = require('whoisjs').whois
who = new whois

#prefixes = [ "yotta", "zetta", "exa", "peta", "tera", "giga", "mega", "kilo", "hecto", "deka", "deci", "centi", "milli", "micro", "nano", "pico", "femto", "atto", "zepto", "yocto" ]
#suffixes = [ "meter", "gram", "second", "ampere", "kelvin", "mole", "candela", "radian", "steradian", "hertz", "newton", "pascal", "joule", "watt", "colomb", "volt", "farad", "ohm", "siemens", "weber", "henry", "lumen", "lux", "becquerel", "gray", "sievert", "katal", "pixel" ]
prefixes = fs.readFileSync process.argv[2], 'utf8'
suffixes = fs.readFileSync process.argv[3], 'utf8'
prefixes = prefixes.trim().split '\n'
suffixes = suffixes.trim().split '\n'
tlds = [ "com" ]

checkAvailable = (help, domain, cb) ->
        who.query domain, (response) ->
                console.log "#{help}: #{domain}" if do response.available

count = 0
for prefix in prefixes
        for suffix in suffixes
                for tld in tlds
                        checkAvailable prefix, "#{prefix}#{suffix}.#{tld}", sys.puts
                        count++

console.log "count: #{count}"