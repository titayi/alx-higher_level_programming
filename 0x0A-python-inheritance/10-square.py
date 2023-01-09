#!/usr/bin/python3
"""
    Defines inheritance from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Defines the class Square
    """
    def __init__(self, size):
        """
            Instantiation with size
            Arg: self, size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
            Returns a super() string of size
        """
        return super().__str__()

    def area(self):
        """ Returns the square area """
        return self.__size ** 2
