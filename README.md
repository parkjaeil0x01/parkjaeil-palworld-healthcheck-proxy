# parkjaeil-palworld-healthcheck-proxy

`parkjaeil-palworld-healthcheck-proxy` is a simple proxy server designed for monitoring the status of specific web services. This project is written in Python and can be containerised using Docker.

## Components

- `app/main.py`: The primary Python script containing the logic for the proxy server. It utilises Flask to implement a simple web server and provides a health check function for certain endpoints.
- `Dockerfile`: This Dockerfile contains instructions for building and running the application as a Docker container.
- `run.sh`: A shell script for building and running the Docker container. This script simplifies the process of building the Docker image and running the container.

## Usage Instructions

### Installing Dependencies

This project utilises Python 3. All necessary dependencies are specified in `requirements.txt`, and can be installed using the following command:

```bash
pip install -r requirements.txt
```

### Run with Docker
```bash
docker run -d --name parkjaeil-palworld-healthcheck-proxy -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock parkjaeil/parkjaeil-palworld-healthcheck-proxy:2024.02.11.23.36-dev
```