#!/usr/bin/python3
"""
    A class that inherits from list class
"""


class MyList(list):
    """
        class that inherits from list
        Arg: list
    """
    def print_sorted(self):
        """
            function that prints ascending sorted list
            Arg: self
        """
        print(sorted(self))
