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

    @property
    def size(self):
        """ Method to return the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

