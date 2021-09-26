import pandas as pd
import json
import csv
import pickle
from flask import Flask
from flask_cors import CORS, cross_origin


def make_json():

    csvFilePath = r'forecast.csv'
    jsonFilePath = r'forecastSegment.json'
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary and add it to data
        for rows in csvReader:

            if(rows['Failure'] == '1'):
                # ID as primary key
                key = rows['TrackSegment']
                data[key] = rows

    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    # print(data)
    # creating a json object
    json_obj = json.dumps(data)

    return json_obj


fSeg = make_json()
print(fSeg)
