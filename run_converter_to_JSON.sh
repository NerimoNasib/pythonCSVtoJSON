#!/bin/bash

read -p "Enter the CSV file name (e.g., input.csv): " csv_file
read -p "Enter the JSON file name (e.g., output.json): " json_file

python csv_to_json_converter.py --csv-file "$csv_file" --json-file "$json_file"

read -p "Press Enter to exit..."