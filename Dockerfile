FROM python:3


RUN apt-get clean && apt-get update && apt-get upgrade -y && \
    apt-get install -y locales

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

