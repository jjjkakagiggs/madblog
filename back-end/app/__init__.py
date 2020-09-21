from flask import Flask
from config import Config
from flask_cors import CORS


cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    cors.init_app(app)

    return app


# 注册 blueprint
def register_blueprints(app):
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')