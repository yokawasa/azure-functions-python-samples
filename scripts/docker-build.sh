#!/bin/sh
set -e -x

cwd=`dirname "$0"`
expr "$0" : "/.*" > /dev/null || cwd=`(cd "$cwd" && pwd)`

DOCKER_ID="<Your Docker ID>"
CONTAINER_IMAGE_NAME="<Container Image Name: azfuncpythonsamples>"

FUNC_PROJECT_DIR="$cwd/../v2functions"

cd $FUNC_PROJECT_DIR
TAG=`cat VERSION`
docker build --tag $DOCKER_ID/$CONTAINER_IMAGE_NAME:$TAG .
