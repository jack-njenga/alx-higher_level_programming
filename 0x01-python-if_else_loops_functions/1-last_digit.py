#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number)
if number < 0:
    rem = number
    while (rem % 10 > 10):
        rem = rem % 10
        if rem < 10:
            if rem < 6:
                print("Last digit of", number, "is", rem, "and is less than 6 and not 0")
            elif rem > 5:
                print("Last digit of", number, "is", rem, "and is greater than 5")
