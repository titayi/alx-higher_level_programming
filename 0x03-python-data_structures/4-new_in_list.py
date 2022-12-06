#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    new_copy = my_list.copy()
    if idx < 0 or idx > list_len - 1:
        return new_copy
    else:
        return new_copy
