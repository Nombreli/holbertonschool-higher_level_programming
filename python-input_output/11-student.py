#!/usr/bin/python3
"""Student class with JSON serialization and reload"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation"""

        if (
            isinstance(attrs, list)
            and all(isinstance(i, str) for i in attrs)
        ):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes from dictionary"""

        for key, value in json.items():
            setattr(self, key, value)
