#!/usr/bin/python3


def lookup(obj):
    """This function return all attrs and methods of a class

    Args:
        obj : class, object or module

    Returns:
        all attrs and methods
    """

    return dir(obj)
