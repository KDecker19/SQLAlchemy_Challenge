# Import the dependencies.
from Flask import Flask, jsonify
from Sqlalchemy import create_engine
from Sqlalchemy.orm import Session
from Sqlalchemy.ext.automap import automap_base
import Datetime as dt
import Numpy as np
from Models import WeatherData

'''Imported Datetime to assist with date calculations. KD '''
#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
base.prepare(engine, reflect=True)

# reflect the tables
Datetime = base.classes.measurement
Station = base.classes.station
Tobs = base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################



# List all routes that are available.

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station"
        f"/api/v1.0/tobs"
    )
@app.route("/api/v1.0/precipitation")
def precipitaion():
    """Return the precipitation data as json"""
    return jsonify(datetime_dict)   

@app.route("/api/v1.0/station")
def station():
    """Return the station data as json"""
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    return jsonify(tobs_dict)   


# Convery query for perciptation to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data as json"""
    datetime_dict = {}
    c_query = session.query(datetime.date, datetime.prcp).\
        filter(datetime.date >= "2016-08-23").all()

    for date, prcp in c_query:
        datetime_dict[date] = prcp
    return jsonify(datetime_dict)


# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/station")
def station():
    """Return the station data as json"""
    station_dict = {}
    s_query = session.query(station.station, station.name, station.latitude, station.longitude, station.elevation).all()

    for station, name, latitude, longitude, elevation in s_query:
        station_dict[station] = name, latitude, longitude, elevation
    return jsonify(station_dict)

# Query the dates and temperature observations of the most active station for the last year of data.

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    tobs_dict = {}
    t_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()

    for date, tobs in t_query:
        tobs_dict[date] = tobs
    return jsonify(tobs_dict)   

# Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    tobs_dict = {}
    t_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()
    
    for date, tobs in t_query:
        tobs_dict[date] = tobs  
    return jsonify(tobs_dict)


# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

@app.route("/api/v1.0/<start>")
def start():
    """Return the start date as Json"""""
    start_dict = {}
    s_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()
    
    for date, tobs in s_query:
        start_dict[date] = tobs
    return jsonify(start_dict)

@app.route("api/v1.0/<start>/<end>")    
def start_end():
    """Return the start and end date as Json"""
    start_end_dict = {}
    se_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()
    
    for date, tobs in se_query:
        start_end_dict[date] = tobs
    return jsonify(start_end_dict)

if __name__ == "__main__":
    app.run(debug=True)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


# Perform Tmin Tavg and Tmax calculations for the dates greater than or equal to the start date.

@app.route("/api/v1.0/<start>")
def start():
    """Return the start date as Json"""
    start_dict = {}
    s_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()

    for date, tobs in s_query:
        start_dict[date] = tobs
    return jsonify(start_dict)


# Perform Tmin Tavg and Tmax calculations for the dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    """Return the start and end date as Json"""
    start_end_dict = {}
    se_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()

    for date, tobs in se_query:
        start_end_dict[date] = tobs
    return jsonify(start_end_dict)


# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

@app.route("/api/v1.0/<start>")
def start():
    """Return the start date as Json"""
    start_dict = {}
    s_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()

    for date, tobs in s_query:
        start_dict[date] = tobs
    return jsonify(start_dict)
# Query the dates and temperature observations of the most active station for the last year of data.

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    tobs_dict = {}
    t_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()

    for date, tobs in t_query:
        tobs_dict[date] = tobs
    return jsonify(tobs_dict)   

# Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    tobs_dict = {}
    t_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()
    
    for date, tobs in t_query:
        tobs_dict[date] = tobs  
    return jsonify(tobs_dict)


# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

@app.route("/api/v1.0/<start>")
def start():
    """Return the start date as Json"""
    start_dict = {}
    s_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()
    
    for date, tobs in s_query:
        start_dict[date] = tobs
    return jsonify(start_dict)

@app.route("/api/v1.0/<start>/<end>")    
def start_end():
    """Return the start and end date as Json"""
    start_end_dict = {}
    se_query = session.query(datetime.date, datetime.tobs).\
        filter(datetime.date >= "2016-08-23").all()
    
    for date, tobs in se_query:
        start_end_dict[date] = tobs
    return jsonify(start_end_dict)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/api/v1.0/<start>")
def start():
    """Return the start date as Json"""
    start_dict = {}
    s_query = session.query(func.min(WeatherData.tobs), func.avg(WeatherData.tobs), func.max(WeatherData.tobs)).\
        filter(WeatherData.date >= start).all()
    
    for min, avg, max in s_query:
        start_dict["Min"] = min
        start_dict["Avg"] = avg
        start_dict["Max"] = max
    
    return jsonify(start_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    """Return the start and end date as Json"""
    start_end_dict = {}
    se_query = session.query(func.min(WeatherData.tobs), func.avg(WeatherData.tobs), func.max(WeatherData.tobs)).\
        filter(WeatherData.date >= start).all()
    
    for min, avg, max in se_query:
        start_end_dict["Min"] = min
        start_end_dict["Avg"] = avg
        start_end_dict["Max"] = max
    
    return jsonify(start_end_dict)


session.close()
    
    


