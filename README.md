# CS5165-LearningDocker

**Put all items in the same directory and naviagte there in a terminal before running the commands**

**Windows Commands**

- build the image:
  -  `docker buildx b -t my-python-container . -f Dockerfile.txt`
    - delete `-f Dockerfile.txt` if the Dockerfile doesn't have a file extension
 
- run the Docker container:
  -  `docker run --rm my-python-container`
      - will run and remove the container after execution, must use terminal output as results
 
  - `docker run -ti my-python-container bash`
    - will allow you to look at the output file in the container after running   

- tag the container
  - `docker tag my-python-container your-dockerhub-username/my-python-container`
 
- save image to .tar file
  - `docker save -o <FILE_NAME>.tar my-python-container`
 
- load image from .tar file
  - `docker load -i <FILE_NAME>.tar`
