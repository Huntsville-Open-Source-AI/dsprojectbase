#!/usr/bin/env bash
source ./00_config/env
docker tag $IMAGENAME $DOCKERHUBUSERNAME/$IMAGENAME:$TAGNAME
docker push $DOCKERHUBUSERNAME/$IMAGENAME

