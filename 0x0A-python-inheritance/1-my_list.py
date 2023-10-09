#!/usr/bin/python3
"""define the class of list"""


class MyList(list):
    """Class inherited from list object"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
