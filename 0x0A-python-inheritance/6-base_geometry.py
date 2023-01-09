#!/usr/bin/python3
"""
    Defines BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry class
    """
    def area(self):
        """
            Public instance method, raises an exception with
            the message- area() is not implemented
        """
        raise Exception("area() is not implemented")
