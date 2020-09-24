from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


cors = CORS()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_plugins(app)

    return app


# 注册 blueprint
def register_blueprints(app):
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


def register_plugins(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)


from app import models

