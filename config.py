import os
# from sqlalchemy import create_engine, text

basedir = os.path.abspath(os.path.dirname(__file__))
DB_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# engine = create_engine(DB_URI)

class Config:
    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False