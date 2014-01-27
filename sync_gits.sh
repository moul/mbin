#!/bin/sh

#set -x

ONLY_CONFIG=$1
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

git_clone() {
    project=$1
    url=$2
    parent_dir=$BASEDIR/$(dirname $1)
    mkdir -p $parent_dir
    cd $parent_dir
    git clone $url
}

handle_gitlab() {
    url=$(get_config $config url)
    ssh_url=$(get_config $config ssh_url)
    token=$(get_config $config token)
    projects=$(gitlab-repos-paths.coffee $url $token)
    for project in $projects; do
        git_clone $project $ssh_url:$project
    done
}

github_repos_paths() {
    token="$1"
    page="$2"
    projects=$(curl -s -H "Authorization: token $token" "https://api.github.com/user/repos?page=$page" | grep full_name | cut -d\" -f4)
    count=$(echo $projects | sed 's/[^\ ]//g' | wc -c)
    if [ "$count" == 30 ]; then
        # FIXME: aggregate
        echo $projects
    else
        echo $projects
    fi
}

handle_github() {
    echo $config github
    token=$(get_config $config token)
    projects=$(github_repos_paths $token 1)
    echo $projects
    for project in $projects; do
        git_clone $project git@github.com:$project
    done
}

handle_project() {
    type=$1
    config=$2
    case $type in
        gitlab) handle_gitlab $config ;;
        github) handle_github $config ;;
    esac
}

if [ -n $ONLY_CONFIG ]; then
    type=$(get_config $ONLY_CONFIG type)
    handle_project $type $ONLY_CONFIG
else
    CONFIGS=$(get_configs)
    for config in $CONFIGS; do
        echo "[$config]"
        type=$(get_config $config type)
        handle_project $type $config
    done
fi
