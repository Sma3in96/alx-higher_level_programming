#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./{} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif not (argv[2] in "+-*/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = argv[1]
        b = argv[3]
        if (argv[2] == '+'):
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        if (argv[2] == '-'):
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        if (argv[2] == '*'):
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        if (argv[2] == '/'):
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
    exit(0)
