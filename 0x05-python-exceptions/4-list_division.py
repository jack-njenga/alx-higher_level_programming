#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(list_length):
        ans = 0
        try:
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0
            try:
                ans = (my_list_1[i] / my_list_2[i])
            except (TypeError, ValueError):
                print("wrong type")
                ans = 0
            except ZeroDivisionError:
                print("division by 0")
                ans = 0
            except IndexError:
                print("out of range")
                ans = 0
        finally:
            my_list.append(ans)

        return (my_list)
