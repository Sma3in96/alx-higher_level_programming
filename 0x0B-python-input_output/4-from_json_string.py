#!/usr/bin/python3
"""from JSON to obj"""
import json


def from_json_string(my_str):
    """function returns obj from JSON"""
    return json.loads(my_str)
