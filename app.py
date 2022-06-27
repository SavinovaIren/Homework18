
from flask_restx import Api
from config import Config
from flask import Flask

from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


# функция создания основного объекта views
def create_app(Config: Config):
    application = Flask(__name__)
    application.config.from_object(Config)
    configure_app(application)
    application.app_context().push()
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)

app = create_app(Config())

if __name__ == '__main__':
    app.run(Config.HOST, Config.PORT)
#Config.HOST, Config.PORT