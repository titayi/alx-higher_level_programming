#!/usr/bin/python3
""" Defining class Square """


class Square:
    """ Defining the square """
    def __init__(self, size=0, position=(0, 0)):
        """ Args:
            self - Param 1
            size - Param 2
            position - param 3

            Checking for typeError and ValueError
            Initializing size """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieves the position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints to stdout the square with the character #."""
        if self.__size == 0:
            print("")
            return

        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
