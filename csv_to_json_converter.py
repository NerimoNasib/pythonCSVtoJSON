import csv
import json
import argparse

def csv_to_json(csv_file, json_file):
    data = []

    # Read data from CSV
    with open(csv_file, 'r', encoding='utf-8-sig') as csvfile:  # Use 'utf-8-sig'
        reader = csv.DictReader(csvfile)
        for row in reader:
            related_terms = [term.strip() for term in row["Related Terms"].split(',')] if row["Related Terms"] else []
            data.append([
                row["Term"],
                row["Japanese Term"],
                row["Category"],
                row["Type"],
                related_terms,
                row["ID"]
            ])

    # Write data to JSON
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

    print(f"JSON file '{json_file}' created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV data to JSON.")
    parser.add_argument("--csv-file", required=True, help="Input CSV file path")
    parser.add_argument("--json-file", required=True, help="Output JSON file path")

    args = parser.parse_args()

    try:
        csv_to_json(args.csv_file, args.json_file)
    except FileNotFoundError:
        print(f"Error: CSV file '{args.csv_file}' not found.")
    except csv.Error:
        print(f"Error: Invalid CSV format in file '{args.csv_file}'.")
