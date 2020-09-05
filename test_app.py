import unittest
import json
from app import create_app
from models import setup_db, db, Movie, Actor, Casting
from flask_sqlalchemy import SQLAlchemy


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgresql://localhost:5432/{}".format(self.database_name)
        setup_db(self.app, self.database_path)

        self.director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhNTDFyQXlnNVFKMGV0UzI2ZjRlTiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRqay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwMGJiMzliMzI3YjMwMDEzZWI5YTk5IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTkzMjYwMzcsImV4cCI6MTU5OTQxMjQzNywiYXpwIjoiMGkwVnNoM0V0dXFud2VCQ2Qwczdud3B1WTd4R3hJbnYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTpjYXN0aW5ncyIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6Y2FzdGluZ3MiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6Y2FzdGluZ3MiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6Y2FzdGluZ3MiLCJwb3N0Om1vdmllcyJdfQ.AXo-03Xv38vGpsapdXju4NAokXxqKz84tgwxxpOwpZ1CRKY0XTMnZFOQki11NlDkbaXOHjpVGdnExfC8svEaBVwnWRCHIICmSxbf57SISWAJOWpB--f6KjjSpzL69EKo1rqgXj1nPYaOKzrEjUtAXN0sz83veXqj0DlTSDyeyC72wfxhCHKKc8Sb0aO9PkM0-K9MvMlxiYDzUvZnNnobbqmJEeH4HClT5oxFLFIIBvcDgV-9Bst4LH2E4YWKYxMZ-Camy8IJ8P2QP5FnMKoBgpjqkrU9Gc91SGRaEp9oG1xplF8RXE_TrV20ysizT06NsjIPN6-8EmH1cZrcJEnYvw'
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '+ self.director}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # self.db.drop_all()
            self.db.create_all()

    def setup_movie(self, title):
        self.client().post('/movies', json={
            'title': title,
            'release_date': "2021-08-25 21:41:41.000000"}, headers=self.headers)

    def setup_actor(self, name):
        self.client().post('/actors', json={
            'name': name,
            'age': 22,
            'gender': "F"}, headers=self.headers)

    def setup_casting(self, title, name):
        self.setup_movie(title)
        movies = [movie.format() for movie in Movie.query.all()]
        movie_id = movies[0]['id']

        self.setup_actor(name)
        actors = [actor.format() for actor in Actor.query.all()]
        actor_id = actors[0]['id']

        self.client().post('/castings', json={
            'actor_id': actor_id,
            'casting_date': "Wed, 30 Sep 2020 19:02:40 GMT",
            'movie_id': movie_id
        }, headers=self.headers)

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_all_movies(self):
        self.setup_movie("Movie1")
        res = self.client().get('/movies', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_get_movie(self):
        self.setup_movie("Movie2")
        movies = [movie.format() for movie in Movie.query.all()]
        movie_id = movies[0]['id']
        res = self.client().get('/movies/{}'.format(movie_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])
        self.assertTrue(len(data['movie']))

    def test_get_non_existing_movie(self):
        res = self.client().get('/movies/100', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_add_movie(self):
        total_movies_before = len(Movie.query.all())
        res = self.client().post('/movies', json={
            'title': "Answer",
            'release_date': "2021-08-25 21:41:41.000000"}, headers=self.headers)
        total_movies_after = len(Movie.query.all())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Movie successfully created!')
        self.assertTrue(data['movie_id'])
        self.assertTrue(total_movies_before < total_movies_after)

    def test_patch_movie(self):
        self.setup_movie("Movie3")
        movies = [movie.format() for movie in Movie.query.all()]
        movie_id = movies[0]['id']
        res = self.client().patch('/movies/{}'.format(movie_id), json={
            'title': 'new title'}, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_patch_non_existing_movie(self):
        res = self.client().patch('/movies/{}'.format(10000), json={
            'title': 'new title'}, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        self.setup_movie("Movie4")
        movies = [movie.format() for movie in Movie.query.all()]
        movie_id = movies[0]['id']
        res = self.client().delete('/movies/{}'.format(movie_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    def test_delete_non_existing_movie(self):
        res = self.client().delete('/movies/{}'.format(100000), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_all_actors(self):
        self.setup_actor("Actor1")
        res = self.client().get('/actors', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['actors']))

    def test_get_actor(self):
        self.setup_actor("Actor2")
        actors = [actor.format() for actor in Actor.query.all()]
        actor_id = actors[0]['id']
        res = self.client().get('/actors/{}'.format(actor_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertTrue(len(data['actor']))

    def test_get_non_existing_actor(self):
        res = self.client().get('/actors/100', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_add_actor(self):
        total_actors_before = len(Actor.query.all())
        res = self.client().post('/actors', json={
            'name': "John Smith",
            'age': 22,
            'gender': "F"}, headers=self.headers)
        total_actors_after = len(Actor.query.all())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Actor successfully created!')
        self.assertTrue(data['actor_id'])
        self.assertTrue(total_actors_before < total_actors_after)

    def test_patch_actor(self):
        self.setup_actor("Actor3")
        actors = [actor.format() for actor in Actor.query.all()]
        actor_id = actors[0]['id']
        res = self.client().patch('/actors/{}'.format(actor_id), json={'name': 'patched name',
            'age': 122}, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_patch_non_existing_actor(self):
        res = self.client().patch('/actors/{}'.format(10000), json={
            'age': 22}, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        self.setup_actor("Actor4")
        actors = [actor.format() for actor in Actor.query.all()]
        actor_id = actors[0]['id']
        res = self.client().delete('/actors/{}'.format(actor_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    def test_delete_non_existing_actor(self):
        res = self.client().delete('/actors/{}'.format(1000000), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_all_castings(self):
        self.setup_casting("Movie5", "Actor5")
        res = self.client().get('/castings', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['castings'])
        self.assertTrue(len(data['castings']))

    def test_delete_casting(self):
        self.setup_casting("Movie6", "Actor6")
        castings = [casting.format() for casting in Casting.query.all()]
        casting_id = castings[0]['id']
        res = self.client().delete('/castings/{}'.format(casting_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['casting_id'])

    def test_delete_non_existing_casting(self):
        res = self.client().delete('/castings/1000', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_castings_by_actor(self):
        self.setup_casting("Movie7", "Actor7")
        actors = [actor.format() for actor in Actor.query.all()]
        actor_id = actors[0]['id']
        res = self.client().get('/actors/{}/castings'.format(actor_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])
        self.assertTrue(data['castings'])

    def test_get_castings_by_movie(self):
        self.setup_casting("Movie8", "Actor8")
        movies = [movie.format() for movie in Movie.query.all()]
        movie_id = movies[0]['id']
        res = self.client().get('/movies/{}/castings'.format(movie_id), headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])
        self.assertTrue(data['castings'])


if __name__ == '__main__':
    unittest.main()
