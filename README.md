# Heroku Django Template for Genechat

An template for Django 1.11.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Using Python 2.7 

## How to Use

To use this project, follow these steps:

1. Clone this project
2. Install requirements from requirements.txt:
	
	$ pip install -r requirements.txt
	
## Configure Database. This project is using postgresql. if you have it installed, do the following:
	
	$ psql
	$ CREATEDB genechat;
	$ CREATE ROLE user WITH LOGIN PASSWORD 'password';
	$ GRANT ALL PRIVILEGES ON DATABASE genechat TO user;
	$ ALTER USER user CREATEDB;

## authenticate in heroku

	$ heroku login

## Test Locally

	$ heroku local web

## authenticate in heroku

	$ heroku login

## Deployment to Heroku
	
	$ heroku 
    $ heroku create
    $ git push heroku master
    $ heroku run python manage.py migrate

## Based in the following project: https://github.com/heroku/heroku-django-template