#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def cal_add(a, b):
    print("{} + {} = {}".format(a, b, add(a, b)))


def cal_sub(a, b):
    print("{} + {} = {}".format(a, b, sub(a, b)))


def cal_mul(a, b):
    print("{} + {} = {}".format(a, b, mul(a, b)))


def cal_div(a, b):
    print("{} + {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    a = 10
    b = 5

    cal_add(a, b)
    cal_sub(a, b)
    cal_mul(a, b)
    cal_div(a, b)
