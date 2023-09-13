#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in a_dictionary:
        new_dict[key] = map(lambda x: x * 2, a_dictionary[key])
    return new_dict
