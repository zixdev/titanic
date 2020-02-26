FROM python:3.7-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
RUN apk add --update --no-cache
COPY ./requirements.txt /app/requirements.txt
RUN chmod +x /app/requirements.txt

# install postgres
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r requirements.txt

RUN apk del .temp-build-deps


# copy project
COPY . /app/
