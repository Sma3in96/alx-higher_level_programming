#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 0:
        print("0 argments.")
    elif len(argv) == 1:
        print("1 argment :")
        print("1: {}".format(argv[0]))
    elif len(argv) > 1:
        print("{} arguments :".format(len(argv)))
        for i in range(0, len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
