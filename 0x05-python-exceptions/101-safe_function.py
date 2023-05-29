#!/usr/bin/python3
import sys as s

def safe_function(fct, *args):
    try:
        n = fct(*args)
        return (n)
    except Exception as err:
        s.stderr.write("Exception: {}\n".format(err))
        return (None)
