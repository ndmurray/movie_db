# MovieDB - the Django App for film enthusiasts!

Completed as a part of the Human Computer Interaction Master's program at the University of Michigan, School of Information

## Purpose

Do you ever struggle to decide what to watch? Are you tired of Netflix, Hulu, and other streaming services promoting badly rated films, making quality flicks harder to find? Struggle no more! This Django application was designed to allow users to query films by IMDB rating, date range released, genre, actor, and director.

## Data set

This application makes use of the IMDB Database for film metadata, and the Open Movie Database (OMDB) for film descriptions

IMDB Database: https://www.imdb.com/interfaces/

OMDB: http://www.omdbapi.com/

## Data model

Please see movie_db_model.png in the root directory of this repository for a graphical representation of the (MySQL) data model.

## Package Dependencies

certifi==2018.10.15
chardet==3.0.4
defusedxml==0.5.0
Django==2.1.1
django-crispy-forms==1.7.2
django-filter==2.0.0
django-test-without-migrations==0.6
idna==2.7
mysqlclient==1.3.13
oauthlib==2.1.0
PyJWT==1.6.4
python3-openid==3.1.0
pytz==2018.5
requests==2.20.0
requests-oauthlib==1.0.0
six==1.11.0
social-auth-app-django==3.1.0
social-auth-core==2.0.0
urllib3==1.24.1

