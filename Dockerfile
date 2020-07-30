FROM python:3.7-alpine
MAINTAINER Cam Romero

# avoid buffering python outputs
ENV PYTHOPNUNBUFFERED 1

# copy and install requirements
COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache bash mariadb-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers

RUN pip install -r /requirements.txt

# delete unneeded dependencies
RUN apk del .tmp-build-deps

# copy project to docker
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create user that run the app
RUN adduser -D user
USER user