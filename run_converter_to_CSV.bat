@echo off
set /p json_file="Enter the JSON file name (e.g., input.json): "
set /p csv_file="Enter the CSV file name (e.g., output.csv): "

python json_to_csv_converter.py --json-file %json_file% --csv-file %csv_file%

pause