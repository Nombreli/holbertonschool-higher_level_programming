#!/usr/bin/python3
"""Returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Convert Python object to JSON string"""
    import json
    return json.dumps(my_obj)
