#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    cp_list[idx] = element

    if idx < 0:
        return cp_list
    if idx >= len(my_list):
        return cp_list
    else:
        return cp_list
