#!/usr/bin/python3
""" Defining class Square """


class Square:
    """ Defining the square """
    def __init__(self, size=0):
        """ Args:
            self - Param 1
            size - Param 2
            Checking for typeError and ValueError
            Initializing size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)
