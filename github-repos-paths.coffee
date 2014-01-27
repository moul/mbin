#!/usr/bin/env coffee

token = process.argv[2]

Github = require 'github'

github = new Github version: "3.0.0", debug: true
github.authenticate type: "oauth", token: token

ret = []

callback = (err, res) ->
  if err
    console.error err
    exit 1

  ret.push [repo.full_name for repo in res]

  if github.hasNextPage res
    github.getNextPage res, callback
  else
    console.log ret

github.repos.getAll {}, callback
