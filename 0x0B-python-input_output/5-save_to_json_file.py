#!/usr/bin/python3
"""save json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """my_obj to filename using json representation"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
