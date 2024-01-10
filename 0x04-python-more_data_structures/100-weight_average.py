#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_product = 0
    total_weight = 0

    for score, weight in my_list:
        sum_product += score * weight
        total_weight += weight
    average = sum_product / total_weight
    return average
