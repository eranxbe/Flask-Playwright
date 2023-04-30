from flask import Flask
from .extensions import db


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from .routes.rest import rest
    from .routes.form import form
    app.register_blueprint(rest)
    app.register_blueprint(form)
    return app

