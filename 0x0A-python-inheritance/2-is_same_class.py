#!/usr/bin/python3
"""
    Module checks for an exact instance of a specified class
"""


def is_same_class(obj, a_class):
    """
        Function returns True if object is exactly an instance
        of specified class; otherwise False
        Arg: obj, a_class
    """
    return True if type(obj) is a_class else False
