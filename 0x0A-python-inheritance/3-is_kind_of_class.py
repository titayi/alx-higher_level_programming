#!/usr/bin/python3
"""
    Checks if the object is an instance of, or is an instance
    of a class inherited from specified class
"""


def is_kind_of_class(obj, a_class):
    """
        Function that returns True if object is an instance of, or
        object is an instance of a class inherited from specified
        class; otherwise False

        Arg: obj, a_class
    """
    return isinstance(obj, a_class)
