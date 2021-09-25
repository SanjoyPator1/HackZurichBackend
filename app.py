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
from flask import jsonify


# FLASK code
app = Flask(__name__)  # creating the Flask class object


@app.route('/')
def home():
    return "hello, this is our flask backend"

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


# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)
if __name__ == '__main__':
    app.run(debug=True)
