#!/bin/sh

#set -x

BASEDIR=$HOME/Git
CONFIG=$HOME/.gitlabjs.yml

get_configs() {
    cat $CONFIG | grep -vE '^#' | grep '^\[' | sed 's/^\[//;s/\]$//'
}

get_config() {
    config=$1
    key=$2
    cat $CONFIG | grep -vE '^#' | grep "^\[${config}" -A 100 | grep "^${key}.*=.*" | head -n 1 | cut -d= -f2 | sed 's/\ //g'
}

cd $BASEDIR

handle_gitlab() {
    host=$(get_config $config host)
    token=$(get_config $config token)
    projects=$(gitlab-repos-paths.coffee $host $token)
    echo "$projects"
}

handle_github() {
    echo $config github
    user=$(get_config $config user)
    token=$(get_config $config token)
}

CONFIGS=$(get_configs)
for config in $CONFIGS; do
    echo "[$config]"
    type=$(get_config $config type)
    case $type in
        gitlab) handle_gitlab $config ;;
        github) handle_github $config ;;
    esac
done
