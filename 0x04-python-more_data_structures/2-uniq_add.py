#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    summ = 0
    for i in my_list:
        if i in unique:
            continue
        unique.append(i)
    for i in unique:
        summ += i
    return summ
