#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
It includes methods for area calculation and integer validation.
"""


class BaseGeometry:
    """A class representing base geometry with validation tools."""

    def area(self):
        """
        Public instance method that raises an Exception.
        The message should be 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value passed to it.
        Args:
            name (str): The name of the parameter, always a string.
            value (int): The value to be validated as a positive integer.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
