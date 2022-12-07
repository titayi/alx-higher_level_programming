#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for t in a_dictionary:
        new_dictionary[t] = a_dictionary[t] * 2
    return new_dictionary
