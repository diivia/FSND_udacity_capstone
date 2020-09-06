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


#### Heroku URL

```
https://capstone-jk.herokuapp.com/
```

Bearer token valid at time of submission:
Casting director
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhNTDFyQXlnNVFKMGV0UzI2ZjRlTiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY1M2NhODdhZTI0MzcwMDZkOGE5ODZhIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTk0MTQ2MzksImV4cCI6MTU5OTUwMTAzOSwiYXpwIjoiMGkwVnNoM0V0dXFud2VCQ2Qwczdud3B1WTd4R3hJbnYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTpjYXN0aW5ncyIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6Y2FzdGluZ3MiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6Y2FzdGluZ3MiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6Y2FzdGluZ3MiLCJwb3N0Om1vdmllcyJdfQ.lG9b6tX06q5EO2RxDaeHPvQNkn6pRPH3XoRmY_DlODsQN_V71EO3sLqCviBhwM1Zgn6Eg_eUq6uQjuA96_biBTWNgSl2B6_wQCQItDIoLFZEa949m8VSx0ZY_iEunNloe2PVu2LSOxOhdzWZ2Y0YG1-xdC2sFZ0VZSeGxTKjav7r9LUenyis6UJwqKkRs6HPJKDFDrBfrvOwG1AM29_yS6eZ0VAag7aXQrkTEMHUtMJ39ioA4-fHv81mdujQfi0jNSSPwFYnrnFbZQKKjIzklE2pCtISMK_SX4jlB2SGEPF5jK56_p_446Q4H9v2fxCxy3NTHdFUlzOzy_Chy-I04w
```

Casting assistant
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhNTDFyQXlnNVFKMGV0UzI2ZjRlTiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY1NTBhYWM3M2NjMjgwMDZkMzA3Y2Q3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTk0MTQyNTYsImV4cCI6MTU5OTUwMDY1NiwiYXpwIjoiMGkwVnNoM0V0dXFud2VCQ2Qwczdud3B1WTd4R3hJbnYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6Y2FzdGluZ3MiLCJnZXQ6bW92aWVzIl19.a28FqGuztBN_vyR7iS7KZvpGZD0Vt2fcKKKcwr16SRNTu7E_43Cfdq2JB4ezUYemtlTiRFm0NaBDSo7O-50NfbSWKfIrJBOrYpCSAe-SP0WBsU85oB3Sn2-AuuXgC7IvemOB-OtdrdcLKfYVrhKpMngihF589hqdKVihJ3oVFzsJSKQ3om0hnFW0ghXuAK2-XGidDhHz6fO-KUUwgL6j-_POEuwuJpESOXWYnmGNrZswc7FL-ezzYk7Ki8U5RZKZyidz4l90TdQIQe3M0v71YnRyspBJWSls5l82OQN7-rnxl6Y9a7IV75PQz0h3kyN8RoSWJsvzv7RoNZbk-fd-6w
```

#### Roles-based access control (RBAC) 
Two roles are created:
* Casting Assistant - only can search for movies, actors and castings
* Casting Director - has full access and permissions for CRUD 

##### Getting token:
To get token for casting director and castin assistant go to following URL:
```bash
https://fsndjk.eu.auth0.com/authorize?audience=capstone&response_type=token&client_id=0i0Vsh3EtuqnweBCd0s7nwpuY7xGxInv&redirect_uri=https://capstone-jk.herokuapp.com
```
Login with credentials for casting director:
```
- director@jkudacity.com
- Password123 
```  
Login with credentials for casting assistant:
```bash
 - assistant@jkudacity.com
 - Password123
```
And get token from response URL

### Backend
The ./capstone directory contains a completed Flask and SQLAlchemy server.

### Frontend
Frontend not implemented.
 
## Endpoints
### Testing endpoints
* Postman test collection included in the project folder with the bearer token for the Casting Director and Cating Assistant authorizations.
* It's possible to test endpoints with curl request, for example:
```bash
curl https://capstone-jk.herokuapp.com/actors -X GET -H 'Authorization: Bearer <token>'
```  
token should be replaced with valid token for Casting Director
* Unittests for endpoints are created using unittest library. To run unittests update `self.director` variable in `MyTestCase#setUp` for correct director bearer token and from virtual env execute
```bash                                                                                  
 python test_app.py
```

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
    'message': "Resourse not Found"
}

- 400 Bad Request
{
    'error': 400,
    'message': "Bad Request"
}

- 401 Unauthorized
{
	'error': 401,
    'message': "Unauthorized Error"
}
```