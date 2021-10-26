# pull official base image
FROM python:3.8.10-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY ./src .

RUN mkdir -p /log


RUN groupadd nobody && \
  chown -R nobody:nobody /log && \
  chmod +x start.sh

USER nobody

# run gunicorn
CMD [ "./start.sh" ]

