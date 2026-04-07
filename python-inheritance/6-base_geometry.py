#!/usr/bin/python3
"""
This module defines a class BaseGeometry
with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class with an area method
    that raises an Exception.
    """

    def area(self):
        """
        Raises an Exception indicating that
        area() is not implemented.
        """
        raise Exception("area() is not implemented")
