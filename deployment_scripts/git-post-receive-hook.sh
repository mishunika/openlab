#!/bin/bash
PROJECT_ROOT="$HOME/openlab"

while read oldrev newrev refname
do
    branch=$(git rev-parse --symbolic --abbrev-ref $refname)
    if [ "master" == "$branch" ]; then
        GIT_WORK_TREE="$PROJECT_ROOT" git checkout -f master
        cd "$PROJECT_ROOT/deployment_scripts"
        docker-compose -p openlab kill web
        docker-compose -p openlab build web
        docker-compose -p openlab up -d --no-recreate
    fi
done
