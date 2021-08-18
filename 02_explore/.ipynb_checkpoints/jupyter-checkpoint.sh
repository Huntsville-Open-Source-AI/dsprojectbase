#!/usr/bin/env bash
docker run --rm -d \
	--name jupyter \
	-p 8888:8888 \
	-e JUPYTER_ENABLE_LAB=yes \
	-v "${PWD}":/home/jovyan/work \
	-v "${PWD}/../01_data:/home/jovian/work/data" \
	jupyter/datascience-notebook:latest && \
sleep 3 && \
docker logs jupyter

