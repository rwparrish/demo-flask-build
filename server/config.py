from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__) #create an instance of the Flask class called app (this is the app object)
app.secret_key = os.getenv("FLASK-SECRET") #set the secret key for the app