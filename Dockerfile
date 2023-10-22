FROM python:3.10.11-slim
LABEL maintainer="anton.komarov.pd@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt

COPY . .
