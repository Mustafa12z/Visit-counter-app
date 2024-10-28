# Visit Counter Web Application

## Overview

The **Visit Counter Web Application** is a simple and elegant web application that keeps track of the number of visits to the page. Built with a sleek HTML and CSS front-end, this project provides a visually appealing interface for users to interact with. The project includes both Docker and Docker Compose configurations to support different use cases. You can either use Docker to manually build and run the container or take advantage of Docker Compose for streamlined multi-service setups.

## Project Structure

```
challenge
├── templates
│   ├── index.html
│   ├── visitcounter.html
├── venv
├── app.py
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Features

- **Real-time Visit Tracking**: The application counts and displays the number of visits dynamically.
- **Modern User Interface**: The front-end is crafted with HTML and CSS to provide an engaging user experience.
- **Dockerized Deployment**: The app is containerized, ensuring consistent performance and easy deployment across various environments.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:
- **Docker**: You can install Docker by following the official installation guide [here](https://docs.docker.com/get-docker/).

### Setting Up the Project

1. **Clone the Repository**:
   Begin by cloning the repository to your local machine.
   ```bash
   git clone https://github.com/Mustafa12z/Visit-counter-app.git
   cd visit-counter-app/challenge
   ```

2. **Using Docker**

   If you'd like to build and run the application using Docker alone, follow these steps:

   - **Build the Docker Image**:
     Use the following command to build the Docker image from the Dockerfile. This step packages the application and its dependencies into a Docker image.
     ```bash
     docker build -t visit-counter .
     ```

   - **Run the Container**:
     After building the image, you can start a container based on this image. This command maps port 5000 on your local machine to port 5000 in the container, making the app accessible locally.
     ```bash
     docker run -p 5000:5000 visit-counter
     ```

   - **Access the Application**:
     Once the container is running, open your browser and go to `http://localhost:5000` to view the visit counter in action.

3. **Using Docker Compose**

   If you prefer a more streamlined approach, Docker Compose allows you to manage multi-container setups and handle dependencies more conveniently. Here’s how to set up and run the application with Docker Compose:

   - **Start the Application with Docker Compose**:
     Use the following command to start the services defined in the `docker-compose.yml` file. Docker Compose will automatically build the image if it hasn't been built yet.
     ```bash
     docker-compose up
     ```

   - **Access the Application**:
     Just as with Docker, the application will be accessible at `http://localhost:5000`.

4. **Stopping the Application**

   - **Stopping the Container with Docker Compose**:
     If you started the application with Docker Compose, you can stop it gracefully with:
     ```bash
     docker-compose down
     ```

   - **Stopping the Container with Docker Only**:
     If you used Docker to start the container, identify the `CONTAINER_ID` by running:
     ```bash
     docker ps
     ```
     Then, stop the container with:
     ```bash
     docker stop [CONTAINER_ID]
     ```