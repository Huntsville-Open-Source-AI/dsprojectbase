#!/usr/bin/env bash
source ./00_config/env
cp ./00_config/requirements.txt ./05_api
cp ./04_models/* ./05_api/app
cp ./05_api/main.py ./05_api/app
cd ./05_api
docker build -t $IMAGENAME .
cd ..
