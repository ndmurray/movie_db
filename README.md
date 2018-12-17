# MovieDB - the Django App for film enthusiasts!

Completed as a part of the Human Computer Interaction Master's program at the University of Michigan, School of Information

## Important notes for SI664 administration team

0. Scroll to dynamically load search results. This app avoids loading everything at once to save load on the browser. Results are set to show 50 at a time on the page, pagination nav found at the bottom of the page.

1. The list view template doubles as the home page: The home page lists users' query results by default. Hover over each search result image to reveal more entity attributes.

2. Users are asked to logon immediately upon accessing the site. Use 'Logout' on the left to logout, and 'Login' on the left to log back in.

3. Add/update/delete: Edit or delete any film from that film's detail page. Add a film via the "New Entry" link in the left navigation.

4. Finally, seeking 50 points extra credit for implementing extra filters


## To launch the app

1. Clone the repo locally or in the cloud, cd into the app folder and launch with:

python manage.py runserver

## Purpose

Do you ever struggle to decide what to watch? Are you tired of Netflix, Hulu, and other streaming services promoting badly rated films, making quality flicks harder to find? Struggle no more! This Django application was designed to allow users to query films by IMDB rating, date range released, genre, actor, and director.

## Data set

This application makes use of the IMDB Database for film metadata, and the Open Movie Database (OMDB) for film descriptions

IMDB Database: https://www.imdb.com/interfaces/

OMDB: http://www.omdbapi.com/

## Data model

![alt text](/static/img/movie_db_model.png)

Please see movie_db_model.png in the root directory of this repository for a graphical representation of the (MySQL) data model.


## Package Dependencies

certifi==2018.11.29
chardet==3.0.4
coreapi==2.3.3
coreschema==0.0.4
defusedxml==0.5.0
Django==2.1.4
django-allauth==0.38.0
django-cors-headers==2.4.0
django-crispy-forms==1.7.2
django-filter==2.0.0
django-rest-auth==0.9.3
django-rest-swagger==2.2.0
djangorestframework==3.9.0
idna==2.7
itypes==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
mysqlclient==1.3.13
oauthlib==2.1.0
openapi-codec==1.3.2
PyJWT==1.7.1
python3-openid==3.1.0
pytz==2018.7
PyYAML==3.13
requests==2.20.1
requests-oauthlib==1.0.0
simplejson==3.16.0
six==1.11.0
social-auth-app-django==3.1.0
social-auth-core==2.0.0
uritemplate==3.0.0
urllib3==1.24.1


