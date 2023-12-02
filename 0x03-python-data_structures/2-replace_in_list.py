#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 :
        return my_list
    for i, elem in enumerate(my_list):
        if i == idx:
            elem = element
    return my_list
