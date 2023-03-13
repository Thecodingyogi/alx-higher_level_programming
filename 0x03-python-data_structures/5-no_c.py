#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        for i in my_string:
            new_string = my_string.remove('c', 'C')
            return new_string
