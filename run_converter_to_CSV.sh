#!/bin/bash

read -p "Enter the JSON file name (e.g., input.json): " json_file
read -p "Enter the CSV file name (e.g., output.csv): " csv_file

python json_to_csv_converter.py --json-file "$json_file" --csv-file "$csv_file"

read -p "Press Enter to exit..."