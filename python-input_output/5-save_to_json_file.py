#!/usr/bin/python3
"""Writes an Object to a text file using JSON representation"""


def save_to_json_file(my_obj, filename):
    """Save Python object as JSON into a file"""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
