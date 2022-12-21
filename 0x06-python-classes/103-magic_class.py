#!/usr/bin/python3
""" Imported a module """

import math
""" Defining the MagicClass """


class MagicClass:
    """ Defining th MagicClass """

    def __init__(self, radius=0):
        """ Args:
                self - Param 1
                radius - Param 2

                Initializing """
        self.__radius = radius

        if type(radius) is not and type(radius) is not float:
            raise TypeError("Radius must be a number")
        self.__radius = radius

    def area(self):
        """ Return the area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Return the circumference """
        return (2 * math.pi) * self.__radius
