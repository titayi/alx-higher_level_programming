#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    new_tuple = ()
    if str_len == 0:
        new_tuple =  0, "None"
    else:
        new_tuple = str_len, sentence[0]
    return new_tuple
