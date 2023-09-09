#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    temp = ""
    for i in range(0, len(my_string)):
        if not (my_string[i] in "cC"):
            temp += my_string[i]
    return temp
