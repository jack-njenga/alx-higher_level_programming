#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    _sum, i = 0, 1

    while i < len(argv):
        _sum = _sum + int(argv[i])
        i = i + 1

    print("{:}".format(_sum))
