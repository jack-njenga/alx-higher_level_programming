#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    ln = len(argv) - 1
    if ln == 0:
        print("0 arguments.")
        exit(0)
    if ln == 1:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(ln))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
