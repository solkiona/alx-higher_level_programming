#!/usr/bin/python3
"""
This Module defines a square.
"""
class Square:
    """
    This class defines a square.
    
    Attributes:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        """ Method to initialized the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
