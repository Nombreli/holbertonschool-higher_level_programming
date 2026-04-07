#!/usr/bin/python3
"""
This module defines the Square class
that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Instantiated with size (validated as a positive integer).
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        Format: [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
