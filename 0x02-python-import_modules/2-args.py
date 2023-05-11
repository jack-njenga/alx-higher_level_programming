#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv

    if len(argv) < 2:
        print("{:} arguments.".format(0))
        exit(0)
    elif len(argv) == 2:
        print("{:} argument:".format(1))
    else:
        i = 1
        print("{:} arguments:".format(len(argv) - 1))
        while i < len(argv):
            print("{:}: {:s}".format(i, argv[i]))
            i += 1
