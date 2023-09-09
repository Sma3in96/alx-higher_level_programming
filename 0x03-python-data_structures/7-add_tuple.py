#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp = ()
    for i in range(0, 2):
        if i < len(tuple_a) and i < len(tuple_b):
            temp += (tuple_b[i] + tuple_a[i],)
        elif i >= len(tuple_a):
            temp += (tuple_b[i],)
        elif i >= len(tuple_b):
            temp += (tuple_a[i],)
    return temp
