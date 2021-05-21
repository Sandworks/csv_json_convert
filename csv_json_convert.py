#!/usr/bin/env python3

# Filename: csv_json_convert.py
# Author:   James Sanders
# Version:  1.0

# Import dependencies
import os
import sys
import csv
import json
from pprint import pprint

# JSON basic structure
json_based_list = {
    "devices": [
    ]
}

# Create JSON file.
def create_json_file(csv_file):
    json_file = csv_file.split(".")[0]+".json"
    return json_file

# Check input and output files. Abort if failed.
def file_checker(input_file, output_file):
    # Check input file exist otherwise abort
    if os.path.exists(input_file):
        # Check output file does not exist otherwise abort
        if os.path.exists(output_file):
            print(output_file, "file exist, please rename the destination file.")
            sys.exit()           
    else:
        print(input_file, "does not exist, please check filename.")
        sys.exit()

# Convert CSV from file to JSON 
def csv_to_json(csv_file):
    # Read data from CSV file and convert them into a list
    with open(csv_file, newline="") as file:
        csv_data = list(csv.reader(file))
    # Gather column titles
    col_names = csv_data[0]
    # Add devices to JSON basic strcuture
    for row in range(1, len(csv_data)):
        add_device = {}
        for col in range(len(csv_data[0])):
            add_device.update({col_names[col] : csv_data[row][col] })
        json_based_list["devices"].append(add_device)
    # Return the complete JSON list
    return json_based_list

# Create JSON file
def create_json(json_file, json_data):
    # Create JSON file
    with open(json_file, 'w') as json_file:
        json.dump(json_data, json_file)
    # Print the result
    print("Convertion from CSV to JSON completed successfully. JSON output:")
    pprint(json_data)


# *** MAIN ***

# Check we received correct argument.
if len(sys.argv) == 2:
	csv_file = sys.argv[1]
	
elif len(sys.argv) == 1:
	sys.exit("Usage: {} <csv file>".format(sys.argv[0]))	

elif len(sys.argv) > 2:
	print ("Too many arguments")
	sys.exit()

# Create JSON file
json_file = create_json_file(csv_file)

# Check both existing CSV exist and the new JSON does not exist. Abort if false.
file_checker(csv_file, json_file)

# Read CSV from file and create JSON data
json_data = csv_to_json(csv_file)

# Copy JSON data to JSON file
create_json(json_file, json_data)


