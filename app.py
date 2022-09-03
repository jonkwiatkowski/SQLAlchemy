import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

####################################
# Database Setup
####################################

engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect = True)

# Save reference to table
Measurement = Base.classes.measurement
Station = Base.classes.station

####################################
# Flask Setup
####################################
app = Flask(__name__)

####################################
# Flask Routes
####################################

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a session from Python to the DB
    session = Session(engine)

    # Query precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    # Convert Query results to a dictionary using date as the key and prcp as the value
    precip_list = []

    for date, prcp in results:
        precip_dict = {}
        precip_dict['date'] = date
        precip_dict['prcp'] = prcp
        precip_list.append(precip_dict)

    # Return the JSON representation of the dictionary
    return jsonify(precip_list)

    # Close Session
    session.close()


@app.route("/api/v1.0/stations")
def stations():
    # Create a session from Python to the DB
    session = Session(engine)

    # Query precipitation data
    results = session.query(Station.station, Station.name).all()

    # Convert Query results to a dictionary using date as the key and prcp as the value
    station_list = []

    for station, name in results:
        station_dict = {}
        station_dict['station'] = station
        station_dict['name'] = name
        station_list.append(station_dict)

    # Return JSON representation of all stations from the dataset
    return jsonify(station_list)

    # Close session
    session.close()

@app.route("/api/v1.0/tobs")
def tobs():
    # Create a session from Python to the DB
    session = Session(engine)

    # Query the dates and temperature observations of the most active station for the previous year of data
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= '2016-08-23').group_by(Measurement.date).order_by(Measurement.date).all()

    # Convert Query results to a dictionary using date as the key and tobs as the value
    tobs_list = []

    for date, tobs in results:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        tobs_list.append(tobs_dict)

    # Return a JSON list of temperature observations for the previous year
    return jsonify(tobs_list)

    # Close session
    session.close()

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create a session from Python to the DB
    session = Session(engine)

    # Query the minimum, average, and maximum temperatures for all dates greater than or equal to start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    # Convert query results to a dictionary
    start_tobs = []

    for min, avg, max in results:
        start_tobs_dict = {}
        start_tobs_dict ['TMIN'] = min
        start_tobs_dict ['TAVG'] = avg
        start_tobs_dict ['TMAX'] = max
        start_tobs.append(start_tobs_dict)

    # Return a JSON list of temperature observations for the previous year
    return jsonify(start_tobs)
    
    # Close session
    session.close()

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Create a session from Python to the DB
    session = Session(engine)

    # Query the minimum, average, and maximum temperatures for all dates greater than or equal to start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    # Convert query results to a dictionary
    start_tobs = []

    for min, avg, max in results:
        start_tobs_dict = {}
        start_tobs_dict ['TMIN'] = min
        start_tobs_dict ['TAVG'] = avg
        start_tobs_dict ['TMAX'] = max
        start_tobs.append(start_tobs_dict)

    # Return a JSON list of temperature observations for the previous year
    return jsonify(start_tobs)
    
    # Close session
    session.close()

if __name__ == '__main__':
    app.run(debug = True)

