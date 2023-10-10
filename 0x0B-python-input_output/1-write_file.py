#!/usr/bin/python3
"""write text on a file"""


def write_file(filename="", text=""):
    "put text into a file"
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
