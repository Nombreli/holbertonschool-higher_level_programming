#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and provides a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    Provides an additional method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements are integers.
        """
        print(sorted(self))
