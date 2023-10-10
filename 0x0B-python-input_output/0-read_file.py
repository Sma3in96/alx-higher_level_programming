#!/usr/bin/python3
""" Read from a file """


def read_file(filename=""):
    """read from a file"""
    with open(filename, mode="r", encoding="utf-8") as f_stream:
        text = f_stream.read()
        print(text, end='')
