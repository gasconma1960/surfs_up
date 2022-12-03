from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
engine= create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
engine= create_engine("sqlite:///hawaii.sqlite")
Base= automap_base()
# reflect the tables
Base.prepare(engine, reflect =True)
# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

@app.route("/")
def welcome():
    return
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')