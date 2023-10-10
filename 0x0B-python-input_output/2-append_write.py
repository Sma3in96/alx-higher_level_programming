#!/usr/bin/python3
"""write text on a file"""


def append_write(filename="", text=""):
    "put text into a file"
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
