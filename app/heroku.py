#!/usr/bin/env python

from os import environ
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class Heroku(object):
    """Heroku configurations for flask."""

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # app.secret_key
        config = {}

        config['DEBUG'] = True
        config['SECRET_KEY'] = environ.get('SECRET_KEY')
        config['SERVER_NAME'] = environ.get('SERVER_NAME')

        # SQL-Alchemy
        config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

        # Sentry
        config['SENTRY_DSN'] = environ.get('SENTRY_DSN')

        # Exceptional
        config['EXCEPTIONAL_API_KEY'] = environ.get('EXCEPTIONAL_API_KEY')

        # Flask-GoogleFed
        config['GOOGLE_DOMAIN'] = environ.get('GOOGLE_DOMAIN')

        # Celery w/ RabbitMQ
        if 'RABBITMQ_URL' in environ:
            config['BROKER_URL'] = environ.get('RABBITMQ_URL')
        # Celery w/ RedisCloud
        elif 'REDISCLOUD_URL' in environ:
            config['BROKER_URL'] = environ.get('REDISCLOUD_URL')
            config['BROKER_TRANSPORT'] = environ.get('REDISCLOUD_URL')

        # Mailgun
        if 'MAILGUN_SMTP_SERVER' in environ:
            config['SMTP_SERVER'] = environ.get('MAILGUN_SMTP_SERVER')
            config['SMTP_LOGIN'] = environ.get('MAILGUN_SMTP_LOGIN')
            config['SMTP_PASSWORD'] = environ.get('MAILGUN_SMTP_PASSWORD')
            config['MAIL_SERVER'] = environ.get('MAILGUN_SMTP_SERVER')
            config['MAIL_USERNAME'] = environ.get('MAILGUN_SMTP_LOGIN')
            config['MAIL_PASSWORD'] = environ.get('MAILGUN_SMTP_PASSWORD')
            config['MAIL_USE_TLS'] = True
        # SendGrid
        elif 'SENDGRID_USERNAME' in environ:
            config['SMTP_SERVER'] = 'smtp.sendgrid.net'
            config['SMTP_LOGIN'] = environ.get('SENDGRID_USERNAME')
            config['SMTP_PASSWORD'] = environ.get('SENDGRID_PASSWORD')
            config['MAIL_SERVER'] = 'smtp.sendgrid.net'
            config['MAIL_USERNAME'] = environ.get('SENDGRID_USERNAME')
            config['MAIL_PASSWORD'] = environ.get('SENDGRID_PASSWORD')
            config['MAIL_USE_TLS'] = True
        # Postmark
        elif 'POSTMARK_SMTP_SERVER' in environ:
            config['SMTP_SERVER'] = environ.get('POSTMARK_SMTP_SERVER')
            config['SMTP_LOGIN'] = environ.get('POSTMARK_API_KEY')
            config['SMTP_PASSWORD'] = environ.get('POSTMARK_API_KEY')
            config['MAIL_SERVER'] = environ.get('POSTMARK_SMTP_SERVER')
            config['MAIL_USERNAME'] = environ.get('POSTMARK_API_KEY')
            config['MAIL_PASSWORD'] = environ.get('POSTMARK_API_KEY')
            config['MAIL_USE_TLS'] = True

        # Heroku Redis
        redis_url = environ.get('REDIS_URL')
        if redis_url:
            url = urlparse(redis_url)
            config['REDIS_HOST'] = url.hostname
            config['REDIS_PORT'] = url.port
            config['REDIS_PASSWORD'] = url.password
            config['BROKER_URL'] = redis_url
            config['BROKER_BACKEND'] = config['BROKER_URL']

        # Redis To Go
        redis_url = environ.get('REDISTOGO_URL')
        if redis_url:
            url = urlparse(redis_url)
            config['REDIS_HOST'] = url.hostname
            config['REDIS_PORT'] = url.port
            config['REDIS_PASSWORD'] = url.password
            config['BROKER_URL'] = redis_url
            config['BROKER_BACKEND'] = config['BROKER_URL']

        # Mongolab
        mongolab_uri = environ.get('MONGOLAB_URI')
        if mongolab_uri:
            url = urlparse(mongolab_uri)
            config['MONGO_URI'] = mongolab_uri
            config['MONGODB_USER'] = url.username
            config['MONGODB_USERNAME'] = url.username
            config['MONGODB_PASSWORD'] = url.password
            config['MONGODB_HOST'] = url.hostname
            config['MONGODB_PORT'] = url.port
            config['MONGODB_DB'] = url.path[1:]

        # MongoHQ
        mongohq_uri = environ.get('MONGOHQ_URL')
        if mongohq_uri:
            url = urlparse(mongohq_uri)
            config['MONGO_URI'] = mongohq_uri
            config['MONGODB_USER'] = url.username
            config['MONGODB_PASSWORD'] = url.password
            config['MONGODB_HOST'] = url.hostname
            config['MONGODB_PORT'] = url.port
            config['MONGODB_DB'] = url.path[1:]

        # Cloudant
        cloudant_uri = environ.get('CLOUDANT_URL')
        if cloudant_uri:
            config['COUCHDB_SERVER'] = cloudant_uri

        # Memcachier
        config['CACHE_MEMCACHED_SERVERS'] = environ.get('MEMCACHIER_SERVERS')
        config['CACHE_MEMCACHED_USERNAME'] = environ.get('MEMCACHIER_USERNAME')
        config['CACHE_MEMCACHED_PASSWORD'] = environ.get('MEMCACHIER_PASSWORD')

        for k, v in dict(config).items():
            if v is None:
                del config[k]

        app.config.update(**config)
