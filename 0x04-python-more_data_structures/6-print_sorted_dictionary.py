#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = [key for key in a_dictionary]
    keys.sort()
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
