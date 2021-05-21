# csv_json_convert

**csv_json_convert.py - Convert CSV host list to JSON format**

_James Sanders ' <ciscoguru72' *at* 'yahoo' *dot* 'com' *dot 'au'_

A python script to convert Excel Spreadsheet format to a JSON file. Note: Save the Excel spreadsheet into CSV format before using this script.

I’m a network engineer who enjoys writing Python scripts to make life easy for myself and others. As a Python newbie, I’m always learning to improve my code. I’m keen to hear your thoughts on my code and how I should improve. Also, I’m eager to hear new ideas and meet likewise people who write network-related Python scripts.

## Userguide

**./csv_json_convert.py _[csv file to convert]_**

or 

**python3 csv_json_convert.py _[csv file to convert]_**

The script will convert CSV file into JSON file using the same name used for CSV. For example:

Excel format: Top row must be the names you want to use in JSON name:value pair. This script will automatically calculate the number of columns you have. Line 2 onwards includes the value you wish to in JSON name:value pair. For example:

![Excel Format](https://raw.github.com/Sandworks/csv_json_convert/excel_format.PNG)

./csv_json_host_list.py device_list.csv

Typing the above command will generate into JSON format as shown:

 

Note: Save the Excel spreadsheet into CSV format before using this script.

## Additional Notes:

You can change the object title to whatever you want. For example, change the variable “json_based_list” to whatever you like JSON format to use.

 


