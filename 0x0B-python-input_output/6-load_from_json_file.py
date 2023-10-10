#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """extract from a json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        return json.loads(data)
