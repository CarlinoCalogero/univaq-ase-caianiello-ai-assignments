import json
import os
import csv


def write_json_file(path, json_dictionary):
    file_path = f"{path}.json"
    # Write dictionary to file using json.dump()
    with open(file_path, "w") as f:
        json.dump(json_dictionary, f)


def write_unicode_json_file(path, json_dictionary):
    file_path = f"{path}.json"
    # Write JSON data with Unicode characters to file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(json_dictionary, f, ensure_ascii=False)


def write_text_file(path, text):
    file_path = f"{path}.txt"
    with open(file_path, "w") as f:
        f.write(text)


def write_csv_file(path, field_names, data):
    file_path = f"{path}.csv"
    # Check if file exists
    if not os.path.exists(file_path):
        # File does not exist, create it and add a header
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows([field_names, data])
            # print(f"File '{file_path}' created with initial data.")
    else:
        # File exists, append new rows
        with open(file_path, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows([data])  # Append data without headers
            # print(f"Data appended to existing file '{file_path}'.")
