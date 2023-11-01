# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

RUN apt-get -y update
RUN #apt-get install build-essential -y
RUN apt-get install -y xmlsec1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/