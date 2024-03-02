import csv
import json
import argparse

def json_to_csv(json_data, csv_file):
    # Load JSON data
    data = json.loads(json_data)

    # Specify the CSV file name
    # Write data to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as csvfile:  # Use 'utf-8-sig'
        # Define CSV header
        fieldnames = ["Term", "Japanese Term", "Category", "Type", "Related Terms", "ID"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        for entry in data:
            related_terms = entry[4][0].replace('\n', ' ') if isinstance(entry[4], list) and entry[4] else ""
            row_dict = {
                "Term": entry[0],
                "Japanese Term": entry[1],
                "Category": entry[2],
                "Type": entry[3],
                "Related Terms": related_terms,
                "ID": entry[5]
            }
            writer.writerow(row_dict)

    print(f"CSV file '{csv_file}' created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON data to CSV.")
    parser.add_argument("--json-file", required=True, help="Input JSON file path")
    parser.add_argument("--csv-file", required=True, help="Output CSV file path")

    args = parser.parse_args()

    try:
        with open(args.json_file, 'r', encoding='utf-8') as json_file:
            json_data = json_file.read()
            json_to_csv(json_data, args.csv_file)
    except FileNotFoundError:
        print(f"Error: JSON file '{args.json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{args.json_file}'.")
