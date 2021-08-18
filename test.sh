#!/usr/bin/env sh
curl -i -X POST http://localhost:8000/predict -H "Content-Type: application/json" --data "{\"sepal_length\":5.1,\"sepal_width\":3.8,\"petal_length\":1.9,\"petal_width\":0.4}"
curl -i -X GET http://localhost:8000/docs
curl -i -X GET http://localhost:8000/redoc


