# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Set PYTHONPATH
ENV PYTHONPATH /usr/src/app

# Command to run on container start
CMD ["python", "src/run.py"]
