#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Raises exception since not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
