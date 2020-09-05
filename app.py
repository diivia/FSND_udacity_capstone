from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from models import setup_db, Movie, Actor, Casting
from auth import AuthError, requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def index():
        return jsonify({'message': 'Udacity Capestone Project'})

    @app.route('/movies')
    #@requires_auth(permission='get:movies')
    def load_movies():
        try:
            movies = Movie.query.all()

            if len(movies) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies]
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>')
    @requires_auth(permission='get:movies')
    def find_movie(self, movie_id):
        movie = find_movie_by_id(movie_id)
        try:
            return jsonify({
                'success': True,
                'movie': movie.format()
            })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth(permission='delete:movie')
    def delete_movie(self, movie_id):
        movie = find_movie_by_id(movie_id)
        try:
            movie.delete()

            return jsonify({
                'success': True,
                'movie_id': movie_id
            })
        except Exception:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth(permission='post:movies')
    def add_movie(self):
        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')

        try:
            movie = Movie(title=title, release_date=release_date)
            if movie is None:
                abort(404)
            movie.insert()

            return jsonify({
                'success': True,
                'message': 'Movie successfully created!',
                'movie_id': movie.id
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth(permission='patch:movies')
    def update_movie(self, movie_id):
        data = request.get_json()
        title = data.get('title', None)
        release_date = data.get('release_date', None)

        movie = find_movie_by_id(movie_id)

        if title is not None:
            movie.title = title
        if release_date is not None:
            movie.release_date = release_date
        movie.update()

        return jsonify({
            'success': True,
            'movie': movie.format()
        })

    def find_movie_by_id(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        return movie

    @app.route('/actors')
    @requires_auth(permission='get:actors')
    def load_actors(self):
        try:
            actors = Actor.query.all()

            if len(actors) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in actors]
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>')
    @requires_auth(permission='get:actors')
    def find_actor(self, actor_id):

        actor = find_actor_by_id(actor_id)
        try:
            return jsonify({
                'success': True,
                'actor': actor.format()
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth(permission='delete:actor')
    def delete_actor(self, actor_id):
        actor = find_actor_by_id(actor_id)
        actor.delete()
        try:
            return jsonify({
                'success': True,
                'actor_id': actor_id
            })
        except:
            abort(422)

    def find_actor_by_id(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        return actor

    @app.route('/actors', methods=['POST'])
    @requires_auth(permission='post:actors')
    def add_actor(self):
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')

        try:
            actor = Actor(name, age, gender)
            if actor is None:
                abort(404)
            actor.insert()

            return jsonify({
                'success': True,
                'message': 'Actor successfully created!',
                'actor_id': actor.id
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth(permission='patch:actors')
    def update_actor(self, actor_id):
        data = request.get_json()
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)

        actor = find_actor_by_id(actor_id)

        if name is not None:
            actor.name = name
        if age is not None:
            actor.age = age
        if gender is not None:
            actor.gender = gender
        actor.update()

        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    @app.route('/castings')
    @requires_auth(permission='get:castings')
    def load_castings(self):
        try:
            castings = Casting.query.all()

            if len(castings) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'castings': [casting.format() for casting in castings]
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>/castings')
    @requires_auth(permission='get:castings')
    def load_castings_by_actor(self, actor_id):
        try:
            castings = Casting.query.filter(Casting.actor_id == actor_id).all()

            if len(castings) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'actor_id': actor_id,
                'castings': [casting.format() for casting in castings]
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>/castings')
    @requires_auth(permission='get:castings')
    def load_castings_by_movie(self, movie_id):
        try:
            castings = Casting.query.filter(Casting.movie_id == movie_id).all()

            if len(castings) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'movie_id': movie_id,
                'castings': [casting.format() for casting in castings]
            })
        except:
            abort(422)

    @app.route('/castings', methods=['POST'])
    @requires_auth(permission='post:castings')
    def add_casting(self):
        data = request.get_json()
        actor_id = data.get('actor_id')
        movie_id = data.get('movie_id')
        casting_date = data.get('casting_date')

        try:
            casting = Casting(actor_id=actor_id, movie_id=movie_id, casting_date=casting_date)
            if casting is None:
                abort(404)
            casting.insert()

            return jsonify({
                'success': True,
                'message': 'Casting successfully created!',
                'casting_id': casting.id
            })
        except:
            abort(422)

    @app.route('/castings/<int:casting_id>', methods=['DELETE'])
    @requires_auth(permission='delete:castings')
    def delete_casting(self, casting_id):
        casting = find_casting_by_id(casting_id)
        casting.delete()
        try:

            return jsonify({
                'success': True,
                'casting_id': casting_id
            })
        except:
            abort(422)

    def find_casting_by_id(casting_id):
        casting = Casting.query.filter(Casting.id == casting_id).one_or_none()
        if casting is None:
            abort(404)
        return casting

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(401)
    def unauthorized_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized Error"
        }), 401

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()
# db_drop_and_create_all()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
