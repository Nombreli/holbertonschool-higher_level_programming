#!/usr/bin/python3
"""
This module defines the MyList class
that inherits from list and adds a method to print the list sorted.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    Provides a method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        The original list remains unchanged.
        """
        print(sorted(self))
