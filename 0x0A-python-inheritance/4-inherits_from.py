#!/usr/bin/python3
"""
    checks if the object is an instance of a class
    that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
        Function returns True if the object is an instance
        of a class that inherited from a specified class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
