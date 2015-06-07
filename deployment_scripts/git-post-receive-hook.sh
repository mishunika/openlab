#!/bin/bash
PROJECT_ROOT="$HOME/openlab_deploy"
COMPOSE_PARAMS="-p openlab -f docker-compose-dev.yml"

while read oldrev newrev refname
do
    branch=$(git rev-parse --symbolic --abbrev-ref $refname)
    if [ "develop" == "$branch" ]; then
        GIT_WORK_TREE="$PROJECT_ROOT" git checkout -f develop
        cd "$PROJECT_ROOT/deployment_scripts"
        docker-compose $COMPOSE_PARAMS kill web
        docker-compose $COMPOSE_PARAMS build --no-cache web
        docker-compose $COMPOSE_PARAMS up -d --no-recreate
        docker exec -it openlab_web_1 python manage.py migrate
    fi
done
