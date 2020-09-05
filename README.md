# Full Stack Nanodegree Final Project - Casting Agency

## Motivation
This is my capstone project for Udacity Full Stack Nanodegree.
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.
Casting Agency model consist of Movie, Actor and Casting which allows to create an audition for an actor for specific movie. 

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigting to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


### Environment Variables Setup
```bash
source setup.sh
```

### Running the server
Create Postgres database by typing in console `createdb capstone` 

From within the `./capstone` directory first ensure you are working using your created virtual environment. To create virtual env, execute: 
```bash
python3 -m venv env
virtualenv env
source env/bin/activate
```

From the `/capstone` directory to install dependencies, execute:

```bash
pip install -r requirements.txt
```

From within the `./capstone` directory to run the server, execute:
```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
 
## Endpoints
### Testing endpoints
* Postman test collection included in the project folder with the bearer token for the Executive Producer authorization.
* Unittests for endpoints are created using unittest library.
### API specification
```bash
GET '/movies'
GET '/actors'
GET '/castings'
GET '/movies/<int:movie_id>/castings'
GET '/actors/<int:actor_id>/castings'
GET '/movies/<int:movie_id>'
GET '/actors/<int:actor_id>'
POST '/movies'
POST '/actors'
POST '/castings'
PATCH '/movies/<int:movie_id>'
PATCH '/actors/<int:actor_id>'
DELETE '/movies/<int:movie_id>'
DELETE '/actors/<int:actor_id>'
DELETE '/castings/<int:casting_id>'
```
##### GET '/movies'
- Fetches a list of all movies in the databases.
- Required Authorization: Casting Assistant or Casting Director.
- Request Arguments: None.
- Returns a JSON object:
```bash
{
  "movies": [
    {
      "id": 14,
      "release_date": "Wed, 25 Aug 2021 21:41:41 GMT",
      "title": "Movie1"
    }
  ],
  "success": true
}
```
##### GET '/actors'
- Fetches a list of all actors in the databases.
- Required Authorization: Casting Assistant or Casting Director.
- Request Arguments: None.
- Returns a JSON object:
```bash
{
  "actors": [
    {
      "age": 22,
      "gender": "F",
      "id": 9,
      "name": "Actor3"
    }
  ],
  "success": true
}
```
##### GET '/castings'
- Fetches a list of all castings in the databases.
- Required Authorization: Casting Assistant or Casting Director.
- Request Arguments: None.
- Returns a JSON object:
```bash
{
  "castings": [
    {
      "actor_id": 8,
      "casting_date": "Wed, 30 Sep 2020 19:02:40 GMT",
      "id": 22,
      "movie_id": 12
    }
  ],
  "movie_id": 12,
  "success": true
}
```
##### GET '/movies/<int:movie_id>/castings'
- Fetches a list of all castings for some movie in the databases.
- Required Authorization: Casting Assistant or Casting Director.
- Request Arguments: None.
- Returns a JSON object:
```bash
{
  "castings": [
    {
      "actor_id": 8,
      "casting_date": "Wed, 30 Sep 2020 19:02:40 GMT",
      "id": 22,
      "movie_id": 12
    }
  ],
  "movie_id": 12,
  "success": true
}
```
##### GET '/actors/<int:actor_id>/castings'
- Fetches a list of all castings for some actor in the databases.
- Required Authorization: Casting Assistant or Casting Director.
- Request Arguments: None.
- Returns a JSON object:
```bash
{
  "actor_id": 8,
  "castings": [
    {
      "actor_id": 8,
      "casting_date": "Wed, 30 Sep 2020 19:02:40 GMT",
      "id": 22,
      "movie_id": 12
    }
  ],
  "success": true
}
```
##### GET '/actors/<int:actor_id>'
- Fetches an existing actor entry for with id actor_id.
- Required Authorization: Casting Director.
- Request Arguments: None
- Returns a JSON object
```bash
{
  "actor": {
    "age": 22,
    "gender": "F",
    "id": 45,
    "name": "Actor8"
  },
  "success": true
}
```
##### GET '/movies/<int:movie_id>'
- Fetches an existing movie entry for with id movie_id.
- Required Authorization: Casting Director.
- Request Arguments: None
- Returns a JSON object
```bash
{
  "movie": {
    "id": 64,
    "release_date": "Wed, 25 Aug 2021 21:41:41 GMT",
    "title": "Movie3"
  },
  "success": true
}
```
##### POST '/movies'
- Adds a new movie to the database.
- Required Authorization: Casting Director.
- Request Arguments: <string:title>, <datetime:date>; date must be of format: YYYY-MM-DDTHH:MM:SS
- Returns a JSON object
```bash
{
  "message": "Movie successfully created!",
  "movie_id": 65,
  "success": true
}
```
##### POST '/actors'
- Adds a new actor to the database.
- Required Authorization: Casting Director.
- Request Arguments: <string:name>, <int:age>, <atring:gender>
- Returns a JSON object
```bash
{
  "message": "Actor successfully created!",
  "actor_id": 65,
  "success": true
}
```
##### POST '/castings'
- Adds a new cating to the database.
- Required Authorization: Casting Director.
- Request Arguments: <int:movie_id>, <datetime:date>, <int:actor_id>;
- Returns a JSON object
```bash
{
  "casting_id": 23,
  "message": "Casting successfully created!",
  "success": true
}
```
##### PATCH '/movies/<int:movie_id>'
- Updates an existing movie entry for with id movie_id.
- Required Authorization: Casting Director.
- Request Arguments: <string:title>, <datetime:date>; date must be of format: YYYY-MM-DDTHH:MM:SS
- Returns a JSON object
```bash
{
  "movie": {
    "id": 8,
    "release_date": "Wed, 25 Aug 2021 21:41:41 GMT",
    "title": "Answer Patched"
  },
  "success": true
}
```
##### PATCH '/actors/<int:actor_id>'
- Updates an existing actor entry for with id actor_id.
- Required Authorization: Casting Director.
- Request Arguments: <string:name>, <int:age>, <atring:gender>
- Returns a JSON object
```bash
{
  "actor": {
    "age": 122,
    "gender": "F",
    "id": 8,
    "name": "Actor8"
  },
  "success": true
}
```

##### DELETE '/movies/<int:movie_id>'
- Removes the movie with movie_id.
- Required Authorization: Casting Director.
- Request Arguments: None.
- Returns a JSON object
```bash
{
  "movie_id": 65,
  "success": true
}
```
##### DELETE '/actors/<int:actor_id>'
- Removes the actor with actor_id.
- Required Authorization: Casting Director.
- Request Arguments: None.
- Returns a JSON object
```bash
{
  "actor_id": 8,
  "success": true
}
```
##### DELETE '/castings/<int:casting_id>'
- Removes the casting with cating_id.
- Required Authorization: Casting Director.
- Request Arguments: None.
- Returns a JSON object
```bash
{
  "casting_id": 23,
  "success": true
}
```

##### Error handlers
```bash
- 404 Not Found
{
    'error': 404,
    'message': "Not Found"
}

- 400 Bad Request
{
    'error': 400,
    'message': "Bad Request"
}

- 401 Unauthorized
{
	'error': 401,
    'message': "Unauthorized"
}
```

#### Heroku URL

Bearer token valid at time of submission:


#### Roles-based access control (RBAC) 
Two roles are created:
* Casting Assistant - only can search for movies, actors and castings
* Casting Director - has full access and permissions for CRUD 

##### Getting token:
To get token for casting director go to following URL:
```bash
https://fsndjk.eu.auth0.com/authorize?
  audience=capstone&
  response_type=token&
  client_id=0i0Vsh3EtuqnweBCd0s7nwpuY7xGxInv&
  redirect_uri=http://localhost:5000
```
Login with credentials for casting director:
```bash
- director@jkudacity.com
- Password123 
```
And get tocken from response URL

### Backend
The ./capstone directory contains a completed Flask and SQLAlchemy server.

### Frontend
Frontend not implemented.