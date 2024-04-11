# Import necessary libraries
from flask import Flask, jsonify
import os
import psycopg2

# Set up variable for constructing Flask application
app = Flask(__name__)

# Set variables equal to connections
database = 'gis5572'
user = 'postgres'
password = 'Hyderabad43%'
host = '35.238.64.215'
port = '5432'

# Set variables for additions to GeoJSON for formatting
gj_start = '{"type":"FeatureCollection", "features":['
gj_end = ']}'

# Set up application to perform a function
@app.route('/')
def home():
    
    # Connect to SDE database
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )

    return "GIS5572 - Lab 3"

# Set up application to perform a function
@app.route('/true_temp_gj')
def true_temp_gj():
    
    # Connect to SDE database
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    
    # Set up cursor
    cursor = conn.cursor()
    
    # Create a variable for a query to extract the GeoJSON
    query = "SELECT JSON_AGG(ST_AsGeoJSON(temp_idw_points)) FROM temp_idw_points"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    true_temp_gj = (str(cursor.fetchall())).replace("\'","").replace("[([","").replace("],)]","")
    true_temp_gj_final = gj_start + true_temp_gj + gj_end
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return true_temp_gj_final

# Set up application to perform a function
@app.route('/interp_temp_gj')
def interp_temp_gj():
    
    # Connect to SDE database
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    
    # Set up cursor
    cursor = conn.cursor()
    
    # Create a variable for a query to extract the GeoJSON
    query = "SELECT JSON_AGG(ST_AsGeoJSON(temp_idw_accuracy)) FROM temp_idw_accuracy"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    interp_temp_gj = (str(cursor.fetchall())).replace("\'","").replace("[([","").replace("],)]","")
    interp_temp_gj_final = gj_start + interp_temp_gj + gj_end
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return interp_temp_gj_final

# Set up application to perform a function
@app.route('/true_elev_gj')
def true_elev_gj():
    
    # Connect to SDE database
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    
    # Set up cursor
    cursor = conn.cursor()
    
    # Create a variable for a query to extract the GeoJSON
    query = "SELECT JSON_AGG(ST_AsGeoJSON(digital_elevation_model_5km_points)) FROM digital_elevation_model_5km_points"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    true_elev_gj = str(cursor.fetchall()).replace("[([","").replace("],)]","").replace("'","")
    true_elev_gj_final = gj_start + true_elev_gj + gj_end
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return true_elev_gj_final

# Set up application to perform a function
@app.route('/interp_elev_gj')
def interp_elev_gj():
    
    # Connect to SDE database
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    
    # Set up cursor
    cursor = conn.cursor()
    
    # Create a variable for a query to extract the GeoJSON
    query = "SELECT JSON_AGG(ST_AsGeoJSON(elev_ord_accuracy)) FROM elev_ord_accuracy"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    interp_elev_gj = str(cursor.fetchall()).replace("[([","").replace("],)]","").replace("'","")
    interp_elev_gj_final = gj_start + interp_elev_gj + gj_end
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return interp_elev_gj_final

# Run the application
if __name__ == "__main__":
    app.run(
        debug = True,
        host = "0.0.0.0",
        port = int(os.environ.get("PORT",8080))
    )
