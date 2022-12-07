#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for t in list(a_dictionary.keys()):
        if a_dictionary[t] == value:
            del a_dictionary[t]
    return a_dictionary
