import json


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
