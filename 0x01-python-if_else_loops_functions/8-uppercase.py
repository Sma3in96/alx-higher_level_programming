#!/usr/bin/python3
def uppercase(str):
    strg = ""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            char = chr(ord(i) - 32)
        else:
            char = i
        strg = strg + char
    print("{}".format(strg))
