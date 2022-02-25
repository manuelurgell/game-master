FROM python:3.9-slim

ARG DEBUG=False

# Save DEBUG value to file
RUN echo "${DEBUG}" | tr [:upper:] [:lower:] > /tmp/debug

# Docker Environment
ENV POETRY_VERSION=1.1.11 \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_CREATE=O \
    POETRY_NO_INTERACTION=1 \
    POETRY_NO_ANSI=1

# If is not a dev environment, then don't create .pyc files
RUN if [ $(cat /tmp/debug) != true ]; then export PYTHONDONTWRITEBYTECODE=1; fi

# Install system programs
RUN apt-get update \
    && apt-get install -y nginx $(test "$(cat /tmp/debug)" != "true" && : || echo "git-all") libxml2-dev libxslt1-dev libffi-dev build-essential libssl-dev libpq-dev supervisor --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# app is the folder where the project is saved
RUN mkdir /app
WORKDIR /app

# Install poetry via pip
RUN pip install -U pip
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Install all or main dependencies depending on the environment
RUN poetry install $(test "$(cat /tmp/debug)" != "true" && echo "--no-dev")

# Copy source code of the project
ADD . /app

# Add permissions to run start.sh file
RUN chmod +x /app/conf/start.sh

# Copy nginx conf as default nginx configuration
RUN rm -f /etc/nginx/sites-enabled/default
RUN ln -s /app/conf/nginx /etc/nginx/sites-enabled/default

# Add supervisor conf
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/app.conf

# Remove debug file variable
RUN rm /tmp/debug

# Crete django static files
RUN python /app/manage.py collectstatic --noinput

# Expose nginx port
EXPOSE 8001

# Run using start.sh file
CMD [ "/app/conf/start.sh" ]
