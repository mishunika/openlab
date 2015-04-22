#!/bin/sh

if [ "$1" == "dev" ]; then
  docker-compose -p openlab_dev -f docker-compose-dev.yml $2
elif [ "$1" == "prod" ]; then
  docker-compose -p openlab -f docker-compose.yml $2
fi
