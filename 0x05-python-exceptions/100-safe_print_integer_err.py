#!/usr/bin/python3
import sys as s

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError, Exception) as err:
        print("Exception: {}".format(err), file = s.stderr)
        return (False)
