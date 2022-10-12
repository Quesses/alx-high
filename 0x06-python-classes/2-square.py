#!/usr/bin/python3
"""Square class, learning classes and docstring style coding."""


class Square:
    """ Defines a Square by another class Square

    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0):
        """
        Initialize the square with a size
        size is specified otherwise default size 0 is used

        :param size: integer value > 0.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("sixe must be >= 0")
        
        self.__size = size
