#!/usr/bin/env coffee

host = process.argv[2]
token = process.argv[3]
key_id = process.argv[4]
key_title = process.argv[5]
key_key = process.argv[6]

Gitlab = require 'gitlab'

gitlab = new Gitlab url: host, token: token

#gitlab.projects.show project_id, (project) ->
#  console.log project

#  gitlab.projects.deploy_keys.getKey project_id, key_id, (key) ->
#    console.log keys

gitlab.projects.all (projects) ->
  for project in projects
    do ->
      project_id = project.id
      gitlab.projects.deploy_keys.getKey project_id, key_id, (key) ->
        unless key
          params =
            id: key_id
            title: key_title
            key: key_key
          gitlab.projects.deploy_keys.addKey project_id, params, (err, ret) ->
            console.log err if err
            console.log "Added key-#{key_id} on project-#{project_id}, err=#{err}, ret=#{ret}"
