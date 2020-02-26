FROM python:3.7.5-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN chmod +x /app/requirements.txt
RUN pip install -r requirements.txt


# copy project
COPY . /app/
