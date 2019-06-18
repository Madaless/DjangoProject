FROM alpine:3.9
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

WORKDIR /code/

RUN chmod +x entrypoint.sh
