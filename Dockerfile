# Base image
# FROM ubuntu:22.04
FROM python:3.9-slim

# Evnironment setup
# install app dependencies
RUN apt-get update && apt-get install -y python3

# Set the working directory
WORKDIR /home/data

# Copy Python script and text files to the container
COPY script.py .
COPY IF.txt .
COPY AlwaysRememberUsThisWay.txt .

CMD ["mkdir", "/home/data/output"]

# Run script
RUN python3 script.py