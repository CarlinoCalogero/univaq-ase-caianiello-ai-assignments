import csv


def read_csv_file_as_dictionary(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        # Initialize result dictionary keys
        for field_name in reader.fieldnames:
            data[field_name] = []

        # Populate the dictionary with column values
        for row in reader:
            for column in reader.fieldnames:
                data[column].append(float(row[column]))

    return data
