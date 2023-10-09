#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
