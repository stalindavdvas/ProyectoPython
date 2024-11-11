# Download and Run the Python Project Using Docker

Follow the steps below to download the Docker image of the project and run it on your local machine.

# Prerequisites

Make sure you have the following installed on your system:

**Docker**: [Install Docker](https://docs.docker.com/get-docker/) Install Docker if it is not already installed.

**Git**: You will need Git to clone the repository. If Git is not installed, you can install [Git here](https://git-scm.com/downloads).

# Steps to Download and Run the Docker Image

Step 1: Clone the Repository

Clone the repository from GitHub to your local machine using the following command:

git clone https://github.com/stalindavdvas/ProyectoPython.git

Navigate to the project directory:

cd ProyectoPython

Step 2: Build the Docker Image

If you want to build the Docker image locally, you can use the following command to create the image from the Dockerfile in the project:

docker build -t proyectopython .

Alternatively, the Docker image is already available in a remote repository of Docker Hub, you can pull it using the following command:

docker pull stalinvasco2024/proyectopython:latest

Step 3: Run the Docker Container

To run the container from the Docker image, use the Docker Desktop application and find the image you have created before.

Step 4: Access the Application

Once the container is running, open your browser and go to:

http://localhost:5000

You should now be able to see your Python application running locally.

Step 5: Test the Deployed Project

If you want to test the project without downloading the image, you can visit the link:

https://proyectopython-production.up.railway.app/

The application is deployed on Railway cloud.
