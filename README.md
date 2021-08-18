# Project: 
MLOps and DevSecOps Baseline Project
Created: June 15, 2021

## Purpose: 
Use these steps to build an DevSecOps or MLOps pipeline.
This project was created for the Huntsville Open Source AI group.

## Description:
This project demonstrates how one might build a Data Science template project with MLOps and DevSecOps features.
Follow the steps, read the scripts, and follow their instructions to learn the elements to build a basic pipeline.

Open Source under the GNU AFFERO GPL, see the LICENSE file.

Note: Python 3.3+ (comes with python3-venv installed)

## Steps:

0. Clone the project:
`git clone <url...>`

1. Pull the data sets
2. Explore and wrangle the data with jupyter notebooks.
3. If desired, change the project or image names, edit 00_config/env to change project, image, or dockerhub locations
`PROJECTNAME=<newname>
IMAGENAME=<newname>
DOCKERHUBUSERNAME=<newname>`

4. Install the python venv virtual environment in the project directory (it is ignored in .gitignore)
`./venv_install.sh`

5. Activate the virtual environmnet
`./venv_activate.sh`

6. Install the dependency requirements
`./init.sh`

7. Build the docker-based microservice
`./build.sh`

8. Create and start the detached microservice
`./create.sh`

9. Scan:
Normally some of these scanning steps within scan.sh would be run before containerization and before dynamic application testing.
The SCA, SAST, Dependency Scanning, Container Scanning, and DAST are contained in a single document for demonstration purposes.
`./scan.sh`

8. Test the Microservice API:
On another terminal pytest the microservice's api.
You will see output that shows the /predict, /docs, and /redocs routes successfully executing.
You may also navigate in a browser to localhost/docs for an interactive console and description of the predict functionality.
`./test.sh`

9. Stop the microservice container
`./stop.sh`

10. Cleanup, remove the docker image
`./remove.sh`

## COMING SOON...
TODO: DVC data management instructions
TODO: Containerization for deployment instructions
TODO: Deployment instructions
TODO: Better flow
