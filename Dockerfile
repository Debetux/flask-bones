FROM python:latest

RUN mkdir -p /var/www/flask-docker-starter
WORKDIR /var/www/flask-docker-starter
ADD requirements.txt /var/www/flask-docker-starter/
RUN pip install -r requirements.txt
ADD . /var/www/flask-docker-starter
