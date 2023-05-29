#!/usr/bin/python3
import sys as s

def safe_function(fct, *args):
    try:
        n = fct(*args)
        return (n)
    except Exception as err:
        print("Exception: {}".format(err), file = s.stderr)
        return (None)
