# CS5165-LearningDocker

**Put all items in the same directory and naviagte there in a terminal before running the commands**

## Windows Commands

### build the image:
- `docker buildx b -t my-python-container .`
  - add `-f Dockerfile.txt` if the Dockerfile has a `.txt` extension
 
### run the Docker container:
- `docker run --rm my-python-container`
  - will run and remove the container after execution, must use terminal output as results
- `docker run -ti my-python-container bash`
  - will allow you to look at the output file in the container
  - use `cat /home/data/output/result.txt`

### tag the container
- `docker tag my-python-container <DOCKERHUB_USERNAME>/my-python-container`
 
### save image to .tar file
- `docker save -o <FILE_NAME>.tar my-python-container`
 
### load image from .tar file
- `docker load -i <FILE_NAME>.tar`

### Docker Compose (EXTRA CREDIT):
- download/make `docker-compose.yaml`, then launch containers
  - `docker compose up`
    - command line and docker desktop should display outputs of the 2 containers
  - `docker compose ps --all` to show containers created with docker compose
  - `docker compose down` to remove containers
