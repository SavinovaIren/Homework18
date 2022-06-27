from marshmallow import fields, Schema
from sqlalchemy.orm import relationship

from setup_db import db

class Genre(db.Model):
     __tablename__ = 'genre'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String)
     movies = relationship("Movie")


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    genres = relationship("Genre")
    directors = relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.Integer()
    director_id = fields.Integer()

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()
