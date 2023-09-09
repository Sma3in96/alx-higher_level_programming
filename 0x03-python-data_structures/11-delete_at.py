#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        temp = []
        for i in range(0, len(my_list)):
            if i == idx:
                continue
            else:
                temp.append(my_list[i])
        return temp
