#!/usr/bin/python3
"""Script for adding all arguments to a Python list and saving them to a JSON
file. """

if __name__ == "__main__":
    import sys
    from 5-save_to_json_file import save_to_json_file
    from 6-load_from_json_file import load_from_json_file

    try:
        existing_list = load_from_json_file("add_item.json")
    except Exception:
        existing_list = []

    existing_list.extend(sys.argv[1:])

    save_to_json_file(existing_list, "add_item.json")
