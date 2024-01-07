#!/usr/bin/python3
""" function """


def find_peak(lst):
    """ find peak """
    if not lst:
        return None
    lst.sort()
    return lst[-1]
