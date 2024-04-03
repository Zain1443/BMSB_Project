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

# Set up application to perform a function
@app.route('/true_mn_temp')
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
    query = "SELECT JSON_AGG(ST_AsGeoJSON(mn_clean_weather)) FROM mn_clean_weather"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    true_temp_gj = (str(cursor.fetchall())).replace("\'","").replace("[([","").replace("],)]","")
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return true_temp_gj

# Set up application to perform a function
@app.route('/interp_mn_temp')
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
    query = "SELECT JSON_AGG(ST_AsGeoJSON(ebk_points)) FROM ebk_points"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    interp_temp_gj = (str(cursor.fetchall())).replace("\'","").replace("[([","").replace("],)]","")
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return interp_temp_gj

# Set up application to perform a function
@app.route('/true_mn_elev')
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
    query = "SELECT JSON_AGG(ST_AsGeoJSON(mndem_points)) FROM mndem_points"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    true_elev_gj = str(cursor.fetchall()).replace("[([","").replace("],)]","")
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return true_elev_gj

# Set up application to perform a function
@app.route('/interp_mn_elev')
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
    query = "SELECT JSON_AGG(ST_AsGeoJSON(ebk_dempoints)) FROM ebk_dempoints"
    
    # Execute the query
    cursor.execute(query)
    
    # Restructure the GeoJSON into correct format
    interp_elev_gj = str(cursor.fetchall()).replace("[([","").replace("],)]","")
    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    # Return GeoJSON
    return interp_elev_gj

# Run the application
if __name__ == "__main__":
    app.run(
        debug = True,
        host = "0.0.0.0",
        port = int(os.environ.get("PORT",8080))
    )
