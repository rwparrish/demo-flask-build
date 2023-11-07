from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

app = Flask(__name__) #create an instance of the Flask class called app (this is the app object)
app.secret_key = os.getenv("FLASK-SECRET") #set the secret key for the app
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI") #set the database URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #set the track modifications to false - less noisy terminal

db = SQLAlchemy(app) #create an instance of the SQLAlchemy class called db (this is the db object)
