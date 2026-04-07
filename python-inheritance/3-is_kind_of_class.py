#!/usr/bin/python3
"""
This module provides a function to check
if an object is an instance of a class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class
    or an instance of a subclass of a_class,
    otherwise returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or subclass, False otherwise.
    """
    return isinstance(obj, a_class)
