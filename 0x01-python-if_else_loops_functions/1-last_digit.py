#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = number * -1
    while (rem > 10):
        rem = rem % 10
        if rem == 0:
            print("Last digit of", number, "is", rem, "and is 0")
        elif rem < 10:
            _rem = "-" + str(rem)
            print("Last digit of", number, "is", _rem, "and is less than 6 and not 0")
        else:
            continue
else:
    rem = number
    while (rem > 10):
        rem = rem % 10
        if rem == 0:
            print("Last digit of", number, "is", rem, "and is 0")
        elif rem < 10:
            if rem < 6:
                print("Last digit of", number, "is", rem, "and is less than 6 and not 0")
            elif rem > 5:
                print("Last digit of", number, "is", rem, "and is greater than 5")
        else:
            continue
