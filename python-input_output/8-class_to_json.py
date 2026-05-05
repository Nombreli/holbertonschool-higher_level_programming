#!/usr/bin/python3
"""Returns dictionary description of an object for JSON serialization"""


def class_to_json(obj):
    """Returns dictionary representation of a class instance"""
    return obj.__dict__
