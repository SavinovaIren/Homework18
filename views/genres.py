from flask_restx import Resource, Namespace
from models import Genre
from setup_db import db
from models import genres_schema, genre_schema

genre_ns = Namespace('genres')

@genre_ns.route("/")
class GenresViews(Resource):
    def get(self):
        """GET /genres — получить все жанры."""
        genre = db.session.query(Genre).all()

        return genres_schema.dump(genre), 200

@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    def get(self, uid):
        """GET /genres/3 — получить жанр по ID."""
        genre = db.session.query(Genre).get(uid)

        return genre_schema.dump(genre), 200