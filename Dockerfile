# python 3.11 image
FROM python:3.11-slim-bookworm

ARG REPO_URL="https://github.com/CS3321-Spring-2024/Team4_Project.git"
ARG BRANCH="main"
ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD=https://install.python-poetry.org
ENV PATH="$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt update \
  && apt upgrade -y \
  && apt-get install -y --no-install-recommends --no-install-suggests curl git bash gcc \
  && ln -sf /bin/bash /bin/sh \ 
  && curl -sSL ${POETRY_DOWNLOAD} | python3 - --version ${POETRY_VERSION}


WORKDIR /tmp/
RUN git clone ${REPO_URL}
WORKDIR  /tmp/Team4_Project

RUN poetry install

EXPOSE 80

CMD ["python", "/tmp/Team4_Project/src/weather_api/__init__.py"]





