
from sys import argv
from math import *


def error(s):
    print(s)
    exit(84)


def print_usage():
    print("USAGE\n"
          "\t./206neutrions n a h sd\n"
          "DESCRIPTION\n"
          "\tn\tnumber of values\n"
          "\ta\tarithmetic mean\n"
          "\th\tharmonic mean\n"
          "\tsd\tstandard deviation")
    exit(0)


def get_input():
    print("Enter next value: ", end='')

    arg = input()
    if arg == "END":
        exit(0)
    try:
        ret = float(arg)
    except ValueError:
        exit(84)
    if ret == 0:
        exit(84)
    return ret


def usage_check():
    if len(argv) == 2 and (argv[1] == "-h" or argv[1] == "--help"):
        print_usage()


def error_handling():
    if len(argv) != 5:
        error("Invalid number of arguments")
    n = float(argv[1])
    if n < 0:
        error("n must be a positive number or zero")
    a = float(argv[2])
    if a < 0:
        error("a must be a positive number or zero")
    h = float(argv[3])
    if h <= 0:
        error("h must be a number bigger than 0")
    sd = float(argv[4])
    if sd < 0:
        error("sd must be a positive number or zero")
    return a, h, n, sd


def neutrinos(n, a, h, sd):
    arg = get_input()
    s = n * a
    sc = (sd**2 + pow(a, 2)) * n
    n += 1
    a = (s + arg) / n
    q = sqrt((sc + pow(arg, 2)) / n)
    h = n / (1 / arg + (n - 1) / h)
    sd = sqrt((sc + pow(arg, 2)) / n - a**2)

    print("    Number of values:\t{0}".format(n))
    print("    Standard deviation:\t%.2f" % sd)
    print("    Arithmetic mean:\t%.2f" % a)
    print("    Root mean square:\t%.2f" % q)
    print("    Harmonic mean:\t%.2f\n" % h)
    neutrinos(n, a, h, sd)


def main():
    usage_check()
    a, h, n, sd = error_handling()
    neutrinos(n, a, h, sd)