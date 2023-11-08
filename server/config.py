from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

import os

load_dotenv()

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

app = Flask(__name__) #create an instance of the Flask class called app (this is the app object) - why is __name__ passed in here?
app.secret_key = os.getenv("FLASK-SECRET") #set the secret key for the app - What is the purpose of os here?
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI") #set the database URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #set the track modifications to false - less noisy terminal

metadata = MetaData(naming_convention=naming_convention)

db = SQLAlchemy(app=app, metadata=metadata) #create an instance of the SQLAlchemy class called db (this is the db object)

migrate = Migrate(app=app, db=db) #create an instance of the Migrate class called migrate (this is the migrate object)

api = Api(app=app) #create an instance of the Api class called api (this is the api object)

CORS(app)  


# 1. Imports**:
#    - Think of these as tools you're bringing into your workshop. Each tool has a specific purpose, like a hammer for nails, a screwdriver for screws, and so on. These tools (imports) help you build your project.

# 2. Load Environment Variables**:
#    - Imagine you have a secret box where you keep important notes. The `load_dotenv()` function is like opening the box and taking out those notes. These notes contain special instructions and secrets for your project.

# 3. Naming Conventions for Database**:
#    - Naming conventions are like having rules for naming your pets. For example, all your dogs should have names starting with "D." These rules help you name your pets consistently, just like your database tables and parts.

# 4. Create a Flask Application**:
#    - Creating a Flask application is like setting up a workspace in your room for building something. This workspace, called "app," is where you'll build your web project. It's like your workshop.

# Set the Secret Key**:
#    - Think of the secret key as a special key to your diary. Only you know this key, and it keeps your thoughts and secrets safe. It's like a hidden lock for your project.

# Configure the Database**:
#    - Configuring the database is like telling your car where to find the fuel it needs. You're giving your project the address of the database it should use to store and retrieve information.

# Disable Tracking Modifications**:
#    - Turning off tracking modifications is like silencing your phone during an important meeting. It stops your application from constantly telling you about every little change it makes, making your workspace quieter.

# Metadata and SQLAlchemy**:
#    - Metadata and SQLAlchemy are like tools you use to talk to a library full of books. Metadata helps organize the library by naming the sections, and SQLAlchemy is the librarian who helps you find and check out books.

# *Database Migrations**:
#    - Database migrations are like updating a recipe book. As you find new recipes and changes, you update the book so that it always has the latest and tastiest recipes.

# Create a RESTful API**:
#     - Building a RESTful API is like setting up a menu in a restaurant. You create a list of dishes (endpoints) and how customers (other software) can order and enjoy them.

# Cross-Origin Resource Sharing (CORS)**:
#     - Enabling CORS is like allowing people from other neighborhoods to visit your lemonade stand. You put up a sign saying, "Visitors from different streets are welcome!" This way, everyone can enjoy your lemonade.

# In this way, each part of your Flask application can be related to familiar concepts, making it easier to understand their roles and purposes.