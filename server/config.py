from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

import os

load_dotenv()

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

app = Flask(__name__) #create an instance of the Flask class called app (this is the app object)
app.secret_key = os.getenv("FLASK-SECRET") #set the secret key for the app
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI") #set the database URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #set the track modifications to false - less noisy terminal

metadata = MetaData(naming_convention=naming_convention)

db = SQLAlchemy(app=app, metadata=metadata) #create an instance of the SQLAlchemy class called db (this is the db object)

migrate = Migrate(app=app, db=db) #create an instance of the Migrate class called migrate (this is the migrate object)
  