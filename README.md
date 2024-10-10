# CS5165-LearningDocker

**Put all items in the same directory and naviagte there in a terminal before running the commands**

**Windows Commands**

- use this command to build the image:
  -  `docker buildx b -t my-python-container . -f Dockerfile.txt`
 
- use this command to run the Docker container:
  -  `docker run --rm my-python-container`
      - will run and remove the container after execution, must use terminal output as results
 
  - `docker run -ti my-python-container bash`
    - will allow you to look at the output file in the container after running   
