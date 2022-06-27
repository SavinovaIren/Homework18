from flask_restx import Resource, Namespace

from models import Director, directors_schema, director_schema
from setup_db import db

director_ns = Namespace('directors')

@director_ns.route("/")
class DirectorsViews(Resource):
    def get(self):
        """GET /directors — получить всех режиссеров."""
        dir = db.session.query(Director).all()

        return directors_schema.dump(dir), 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid):
        """#GET /directors/3 — получить режиссера по ID."""
        dir = db.session.query(Director).get(uid)
        return director_schema.dump(dir), 200
