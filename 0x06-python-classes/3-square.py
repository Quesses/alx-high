#!/usr/bin/python3
"""Square class, learning classes and docstring style coding."""


class Square:
    """ Defines a Square by another class Suare."""

    def __init__(self, size=0):
        """
        Initialize the square with a size (private instantiation)
        No type / value verification
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("sixe must be >= 0")
