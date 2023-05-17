#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    if not isinstance(roman_string,str):
        return (0)

    ret, num = 0, 0
    roman_nums = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
            }

    for key in roman_string[::-1]:
        curr = roman_nums.get(key, 0)

        if curr >= num:
            ret += curr
        else:
            ret -= curr
        num = curr

    return (ret)

