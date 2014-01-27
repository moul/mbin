#!/usr/bin/env coffee

token = process.argv[2]

Github = require 'github'

github = new Github version: "3.0.0", debug: process.env.DEBUG?
github.authenticate type: "oauth", token: token

ret = []

callback = (err, res) ->
  if err
    console.error err
    process.exit 1

  ret = ret.concat [repo.full_name for repo in res][0]

  if github.hasNextPage res
    github.getNextPage res, callback
  else
    console.log ret.join ' '

github.repos.getAll {}, callback
