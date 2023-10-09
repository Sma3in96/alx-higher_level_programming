#!/usr/bin/python3
"""define the class of list"""


class my_list(list):
    """Class inherited from list object"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
