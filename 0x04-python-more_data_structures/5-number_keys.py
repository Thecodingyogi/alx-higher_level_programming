#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0

    key_list = list(a_dictionary.keys())

    for i in key_list:
        sum += i
    return sum
