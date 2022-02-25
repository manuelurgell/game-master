## Overview
This API is a simple RESTful service that allows to interact with servers and players.
***
## Index
- [Review project](#review-project)
  - [Install project](#install-project)
  - [Environment](#environment)
  - [Run project](#run-project)
  - [API documentation](#api-documentation)
  - [Additional configuration](#additional-configuration)
- [Development](#development)
  - [Install project](#install-project-1)
  - [Clone from GitLab](#clone-from-gitlab-1)
  - [Environment](#environment-1)
  - [Run project](#run-project-1)
  - [Models](#models)
  - [Developing](#developing)
  - [Unit tests](#unit-tests)
  - [API documentation](#api-documentation-1)
  - [Additional configuration](#additional-configuration-1)
***
## Review project

### Install project
- Prerequisites:
  - docker (20.1.8 recommended)
  - docker-compose (1.29.2 recommended)
- Ports:
  - The backend api runs on port `8000` by default.
  - The local database for reviewing runs on port `5432` by default.


### Environment
- Create a .env file with the following contents (defaults are given, feel free to change them):
  ```
  POSTGRES_DB=test
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_HOST=database
  ```
- You are also able to change the ports for the database and backend containers by adding and changing the following variables:
  ```
  POSTGRES_PORT=5432
  BACKEND_PORT=8000
  BACKEND_STATIC_PORT=8001
  ```

### Run project
- Run with docker-compose:
  ```
  docker-compose build
  docker-compose up
  ```

### API documentation
- **Under development...**

### Additional configuration

- You can create a volume for the whole backend application by adding the following variables:
  ```
  APP_LOCAL_VOLUME=/.docker_volumes/backend
  APP_CONTAINER_VOLUME=/app
  ```
- You can set the secret key of the backend app using the following variable:
  ```
  SECRET_KEY
  ```
