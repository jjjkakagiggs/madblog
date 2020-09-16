from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)

    return app


# 注册 blueprint
def register_blueprints(app):
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')