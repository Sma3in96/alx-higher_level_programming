#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("0 argments.")
    elif i == 1:
        print("1 argment :")
        print("1: {}".format(argv[0]))
    elif i > 1:
        print("{} arguments :".format(i))
        for j in range(0, len(i)):
            print("{}: {}".format(j + 1, argv[j]))
