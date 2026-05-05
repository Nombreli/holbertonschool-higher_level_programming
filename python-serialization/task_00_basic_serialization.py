#!/usr/bin/python3
"""Basic serialization module (JSON save/load)"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize dictionary and save it to a JSON file"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON file and return Python dictionary"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
