FROM python:3.10-buster

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        git \
        cmake
RUN pip install poetry
WORKDIR /app
COPY . /app

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD gunicorn --bind :$PORT app:app


