#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    else:
        temp = my_list[:]
        temp[idx] = element
        return temp
