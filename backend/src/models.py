import os
from datetime import datetime

from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "capstone"
database_path = "postgresql://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Movie(db.Model):
    # Autoincrementing, unique primary key
    __tablename__ = 'movies'
    id = Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __repr__(self):
        return f'<Movie title: {self.title}, Release date: {self.release_date}>'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actor(db.Model):
    __tablename__ = 'actors'
    # Autoincrementing, unique primary key
    id = Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(120))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f'<Actor name: {self.name}, Age: {self.age}, Gender: {self.gender}>'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Casting(db.Model):
    __tablename__ = 'castings'
    # Autoincrementing, unique primary key
    id = Column(db.Integer, primary_key=True)
    casting_date = db.Column(db.DateTime)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey(Actor.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'casting_date': self.casting_date,
            'actor_id': self.actor_id,
            'movie_id': self.movie_id
        }

    def __init__(self, actor_id, movie_id, casting_date=datetime.now()):
        self.actor_id = actor_id
        self.movie_id = movie_id
        self.casting_date = casting_date
