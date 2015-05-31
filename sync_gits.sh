#!/bin/sh

#set -x

BASEDIR="$HOME/Git"
CONFIG="$HOME/.gitlabjs.yml"

get_configs() {
    grep -vE '^#' "$CONFIG" | grep '^\[' | sed 's/^\[//;s/\]$//'
}

get_config() {
    config="$1"
    key="$2"
    grep -vE '^#' "$CONFIG" | grep "^\[${config}" -A 100 | grep "^${key}.*=.*" | head -n 1 | cut -d= -f2 | sed 's/\ //g'
}

cd "$BASEDIR"

git_clone() {
    project="$1"
    url="$2"
    parent_dir=$BASEDIR/$(dirname "$1")
    mkdir -p "$parent_dir"
    cd "$parent_dir"
    git clone "$url"
}

handle_gitlab() {
    url=$(get_config "$config" url)
    ssh_url=$(get_config "$config" ssh_url)
    token=$(get_config "$config" token)
    projects=$(gitlab-repos-paths.coffee "$url" "$token")
    for project in $projects; do
        git_clone "$project" "$ssh_url:$project"
    done
}

handle_github() {
    token=$(get_config "$config" token)
    projects=$(github-repos-paths.coffee "$token")
    for project in $projects; do
        git_clone "$project" "git@github.com:$project"
    done
}

handle_project() {
    type="$1"
    config="$2"
    case "$type" in
        gitlab) handle_gitlab "$config" ;;
        github) handle_github "$config" ;;
    esac
}

if [ -z "$1" ]; then
    CONFIGS=$(get_configs)
    for config in $CONFIGS; do
        echo "[$config]"
        type=$(get_config "$config" type)
        handle_project "$type" "$config"
    done
else
    config="$1"
    echo "[$config]"
    type=$(get_config "$config" type)
    handle_project "$type" "$config"
fi
