#!/usr/bin/env bash
source ./00_config/env
docker run -d \
  --name $IMAGENAME \
  -p 8000:5000 \
  $IMAGENAME
