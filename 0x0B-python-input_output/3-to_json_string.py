#!/usr/bin/python3
"""convert a data to Json"""
import json


def to_json_string(my_obj):
    """use dumps to convert obj to json"""
    return json.dump(my_obj)
