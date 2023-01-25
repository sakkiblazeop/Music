# syntax=docker/dockerfile:1
FROM python:3.9.7-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
CMD bash start


