#!/usr/bin/python3

def remove_char_at(_str, n):
    if n < 0 or n >= len(_str):
        return (_str)
    else:
        new_str = _str[:n] + _str[n+1:]
        return (new_str)
