from config import Config


class TestConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = "mysql://root:jjj123456@127.0.0.1:3306/madblog?charset=utf8"
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'edbca'

