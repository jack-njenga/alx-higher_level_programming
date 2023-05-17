#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    t_sum = sum(score * weight for score, weight in my_list)
    t_weight = sum(weight for _, weight in my_list)
    avg = t_sum / t_weight

    return (avg)
