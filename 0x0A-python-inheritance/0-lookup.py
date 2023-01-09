#!/usr/bin/python3
"""
    The module returns list of available attributes and methods of an object
"""


def lookup(obj):
    """
    The function returns a list object
    Arg: obj
    """
    return dir(obj)
