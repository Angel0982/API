#//DOCKERFILE
# Use the base Python 3.7 image
FROM python:3.7-bullseye

# Set the working directory
WORKDIR /api

# Install system dependencies
USER root

RUN apt-get update && apt-get install -y virtualenv

# Create a virtual environment
RUN virtualenv env

# Activate the virtual environment
SHELL ["/bin/bash", "-c"]
RUN source env/bin/activate

# Install required Python packages
COPY . /api/
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP="entrypoint:app"
ENV FLASK_DEBUG="1"
ENV APP_SETTINGS_MODULE="config.default"

# Expose the Flask port
EXPOSE 6001


