from turtle import st
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc

app = Flask(__name__)

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#home route
@app.route("/")
def home():
    return(
        f"<center><h1>Welcome to the Hawaii Climate Analysis Local API</h1></center>"
        f"<center><h3><strong>Choose desired route:</strong></h3></center>"
        f"<center><em>/api/v1.0/precipitation</em></center>"
        f"<center><em>/api/v1.0/stations</em></center>"
        f"<center><em>/api/v1.0/tobs</em></center>"
        f"<center><em>/api/v1.0/start/end</em></center>"
        )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in data set.
    oneYearAgo = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    yearprcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= oneYearAgo).all()

    session.close()

    precipitation = {date: prcp for date, prcp in yearprcp}
    
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

    results = session.query(Station.station).all()

    session.close()

    stationlist = list(np.ravel(results))

    return jsonify(stationlist)

@app.route("/api/v1.0/tobs")
def TOBS():

    oneYearAgo = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    tob = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= oneYearAgo).all()


    session.close()

    toblist = list(np.ravel(tob))

    return jsonify(toblist)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def datestats(start = None, end= None):

    selection = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    if not end:

        startdate = dt.datetime.strptime(start, "%m%d%Y")

        dates = session.query(*selection).filter(Measurement.date >= startdate).all()

        session.close()
        
        toblist = list(np.ravel(dates))

        return jsonify(toblist)

    else:

        startdate = dt.datetime.strptime(start, "%m%d%y")
        enddate = dt.datetime.strptime(end, "%m%d%y")

        dates = session.query(*selection)\
            .filter(Measurement.date >= startdate)\
            .filter(Measurement.date <= enddate).all()

        session.close()
            
        toblist = list(np.ravel(dates))

        return jsonify(toblist)


if __name__ == '__main__':
    app.run(debug=True)
