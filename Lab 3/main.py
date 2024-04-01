#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

database = 'bmsb_project_shared'
user = 'postgres'
password = 'Hyderabad43%'
host = '35.238.64.215'
port = '5432'

@app.route('/minnesota_weather')
def temp_gj():
    
    conn = psycopg2.connect(
        database = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    
    cursor = conn.cursor()
    
    query = "SELECT JSON_AGG(ST_AsGeoJSON(mn_clean_weather)) FROM mn_clean_weather"
    
    cursor.execute(query)
    
    temp_gj = (str(cursor.fetchall())).replace("\'","")
    temp_gj_1 = temp_gj.replace("[([","")
    temp_gj_final = temp_gj_1.replace("],)]","")
    
    cursor.close()
    conn.close()
    
    return temp_gj_final

if __name == "__main__":
    app.run(
        debug = True,
        host = "0.0.0.0",
        port = int(os.environ.get("PORT",8080))
    )

