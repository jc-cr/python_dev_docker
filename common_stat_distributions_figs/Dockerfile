# Use an official Python runtime as a parent image
FROM python:3.8.19-bookworm

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /container_workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /container_workspace
COPY . /container_workspace/

# Install any needed packages specified in requirements.txt
COPY requirements.txt /container_workspace/
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "main.py"]
