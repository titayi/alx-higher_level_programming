#!/usr/bin/python3
"""
    Defines BaseGeometry
"""


class BaseGeometry:
    """
        Defines the class BaseGeometry
    """
    def area(self):
        """
            Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates value

            Arg: self, name, value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
