#!/bin/bash
docker run -d --name parkjaeil-palworld-healthcheck-proxy -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock parkjaeil/parkjaeil-palworld-healthcheck-proxy:2024.02.11.23.36-dev
