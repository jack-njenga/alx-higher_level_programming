#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = str(number)[-1]
str1 = "Last digit of"
str2 = "and is less than 6 and not 0"
if number < 0:
    if rem == "0":
        print(str1, number, "is", rem, "and is 0")
    else:
        _rem = "-" + rem
        print(str1, number, "is", _rem, str2)
else:
    rem = int(rem)
    if (rem < 6 and rem > 0):
        print(str1, number, "is", rem, str2)
    elif (rem == 0):
        print(str1, number, "is", rem, "and is 0")
    else:
        print(str1, number, "is", rem, "and is greater than 5")
