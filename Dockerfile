FROM python:3


RUN apt-get clean && apt-get update && apt-get upgrade -y && \
    apt-get install -y locales

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# EXPOSE $PORT:8000

CMD ["python3", "manage.py", "runserver", "127.0.0.1:$PORT"]