#!/usr/bin/python3
def lookup(obj):
    """
    this function return all attrs and methods of a class
    args:
    obj = class, object or module
    return:
    all attrs and methods
    """

    return (dir(obj))
