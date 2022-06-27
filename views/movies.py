from flask import jsonify, request
from flask_restx import Resource, Namespace

from models import Movie, Genre, Director, movies_schema, movie_schema
from setup_db import db


movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesViews(Resource):
     def get(self):
         """GET /movies — получить все фильмы."""
         movie_with_genre_and_director = db.session.query(Movie.id, Movie.title, Movie.description, Movie.rating,Movie.year,
                                                          Movie.trailer, Genre.name.label('genre'),
                                                          Director.name.label('director')).join(Genre).join(Director)
         # представление возвращает только фильмы с определенным режиссером и жанром по запросу типа: /movies/?director_id=2&genre_id=4
         director_id = request.args.get('director_id')
         genre_id = request.args.get('genre_id')
         year = request.args.get('year')
         """GET /movies?director_id=15 — получить все фильмы режиссера."""
         if director_id:
             movie_with_genre_and_director = movie_with_genre_and_director.filter(Movie.director_id == director_id)
         """GET /movies?genre_id=3 — получить все фильмы жанра"""
         if genre_id:
             movie_with_genre_and_director = movie_with_genre_and_director.filter(Movie.genre_id == genre_id)
         """GET /movies?year=2017 — получить все фильмы за год."""
         if year:
             movie_with_genre_and_director = movie_with_genre_and_director.filter(Movie.year == year)

         all_movies = movie_with_genre_and_director.all()
         return movies_schema.dump(all_movies), 200

     def post(self):
         """POST /movies — создать фильм."""
         req_json = request.json
         new_film = Movie(**req_json)
         with db.session.begin():
             db.session.add(new_film)

         return f"Новый фильм с id {new_film.id} добавлен", 201

@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def put(self, uid):
        movie = db.session.query(Movie).get(uid)
        req_json = request.json
        movie.title = req_json.get('title')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.description = req_json.get('description')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')
        db.session.add(movie)
        db.session.commit()

        return f"Фильм с id {movie.id} обнавлен", 200

    def delete(self, uid):
        movie = db.session.query(Movie).get(uid)
        db.session.delete(movie)
        db.session.commit()

        return f"Фильм с id {movie.id} удален", 201