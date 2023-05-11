#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    l = len(argv) - 1
    if l == 0:
        print("0 arguments.")
        exit(0)
    if l == 1:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(len(argv) - 1))

    i = 1
    while i < len(argv):
        print("{}: {}".format(i, argv[i]))
        i += 1
