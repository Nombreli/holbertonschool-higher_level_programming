#!/usr/bin/python3
"""Returns a Python object represented by a JSON string"""


def from_json_string(my_str):
    """Convert JSON string to Python object"""
    import json
    return json.loads(my_str)
