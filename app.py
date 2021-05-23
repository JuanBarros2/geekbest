from flask import Flask
from ext.api import api
from ext.database import database


def create_app():
    app = Flask(__name__)
    database.init_app()
    api.init_app(app)
    return app
