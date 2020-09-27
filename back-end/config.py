import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:jjj123456@127.0.0.1:3306/madblog?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'edbca'

