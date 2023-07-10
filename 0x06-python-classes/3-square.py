#!/usr/bin/python3
"""This module defines  an Area of a Square
"""
class Square:
    """This class defines the Area of a Square

    Attributes:
        size (int): Size of the Square
    """
    def __init__(self, size=0):
        """This method initializes the attribute size

        Attributes:
            size (int): Size of the Square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area
        """
        return (self.__size ** 2)
