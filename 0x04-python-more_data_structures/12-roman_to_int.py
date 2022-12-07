#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    def_roman = 0
    for t in range(len(roman_string)):
        if t > 0 and roman_num[roman_string[t]] > roman_num[roman_string[t - 1]]:
            def_roman += roman_num[roman_string[t]] - 2 * roman_num[roman_string[t - 1]]
        else:
            def_roman += roman_num[roman_string[t]]
    return def_roman
