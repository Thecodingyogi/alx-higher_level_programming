#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_res = set(my_list)
    uniq_list = list(set_res)
    sum = 0

    for x in uniq_list:
        sum += x
    return sum
