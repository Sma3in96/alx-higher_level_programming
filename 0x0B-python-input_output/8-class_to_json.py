#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """ class to json"""

    d = {}
    if hasattr(obj, "__dict__"):
        d = obj.__dict__.copy()
        return d
