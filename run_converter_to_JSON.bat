@echo off
set /p csv_file="Enter the CSV file name (e.g., input.csv): "
set /p json_file="Enter the JSON file name (e.g., output.json): "

python csv_to_json_converter.py --csv-file %csv_file% --json-file %json_file%

pause