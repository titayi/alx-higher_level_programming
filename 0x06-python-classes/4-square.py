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
        self.__size = size

    @property
    def size(self):
        """ Retrieves the size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size
        Args:
            self - param 1
            value - param 2

            Checks for TypeError and ValueError """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)
