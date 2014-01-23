#!/usr/bin/env coffee

host = process.argv[2]
token = process.argv[3]

Gitlab = require 'gitlab'

gitlab = new Gitlab url: host, token: token

gitlab.projects.all (projects) ->
  console.log [project.path_with_namespace for project in projects][0].join(' ')
