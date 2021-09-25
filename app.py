# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:05:48 2021

@author: asus
"""


import pandas as pd
import json
import csv
import pickle
from flask import Flask


# FLASK code
app = Flask(__name__)  # creating the Flask class object


@app.route("/", methods=['GET'])
# @cross_origin()
def hello():
    data = {"key": "home page value"}
    data1 = json.dumps(data)
    return data1


'''RSSI.csv route'''


@app.route("/rssi", methods=['GET', 'POST'])
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json():

    csvFilePath = r'rssi_test50.csv'
    jsonFilePath = r'rssi.json'
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary and add it to data
        for rows in csvReader:

            # ID as primary key
            key = rows['sl']
            data[key] = rows

    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    print(data)
    # creating a json object
    json_obj = json.dumps(data)

    return json_obj


# reading dummy geo data .json
f = open("dummyGeo.json")
geoJson = json.load(f)

'''Geo Feature'''


@app.route("/geoFeature", methods=['GET', 'POST'])
# Function to convert a CSV to JSON
def get_geo():
    print("geo")
    # print(geoJson)

    # jsonFormat
    features = []
    for gej in geoJson['geo']:
        # variables
        daysUntilNow = gej['daysUntilNow']
        trackId = gej['trackId']
        AreaNumber = gej['AreaNumber']
        long = gej['long']
        lat = gej['lat']
        segNo = gej['segNo']

        coordinates = []
        coordinates.append(long)
        coordinates.append(lat)

        geometry = {
            "type": "Point",
            "coordinates": coordinates
        }

        feature = {
            "type": "Feature",
            "properties": {
                "daysUntilNow": daysUntilNow,
                "trackId": trackId,
                "AreaNumber": AreaNumber,
                "long": long,
                "lat": lat,
                "segNo": segNo
            },
            "geometry": geometry
        }

        features.append(feature)

    featureCollection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(featureCollection)
    json_obj = json.dumps(featureCollection)

    return json_obj


# opening Graph json data
# reading dummy geo data .json
g = open("dummyTimeRssi.json")
grJson = json.load(g)

'''Graph - date - rssi'''


@app.route("/graphRssi", methods=['GET', 'POST'])
# Function to convert a CSV to JSON
def get_graph():
    print("graph")
    # print(grJson)

    # jsonFormat
    graphData = []
    for gej in grJson['graph']:
        # variables
        #print("gej", gej)
        date = gej['date']
        rssi = gej['rssi']

        data = {
            "date": date,
            "rssi": rssi
        }

        graphData.append(data)

    graphJson = {"graph": graphData}

    # print(featureCollection)
    json_obj = json.dumps(graphJson)

    return json_obj


# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
