#!/usr/bin/env python

"""
Description:
Take roman numeral as a string and return it as an integer. 
If the string is not valid return None.

"""
__author__ = "vivek"



import sys
from collections import Counter


def int_value(in_char):
    """
    return integer value of given char. 
    """

    r_dict = dict([('I', 1),
                   ('V', 5),
                   ('X', 10),
                   ('L', 50),
                   ('C', 100),
                   ('D', 500),
                   ('M', 1000)])

    return r_dict[in_char]


def has_valid_roman_chars(in_string):

    valid_chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    valid = True

    for char in in_string:
        if not (char.isalpha() and char.upper() in valid_chars):
            valid = False

    return valid


def has_multiple_DLV(in_st):

    # char frequency in the string
    counter = dict(Counter(in_st))

    not_allowed_multiple = ['D', 'L', 'V']

    # if any frequency is more than 1 for D, L, V - return True.
    for ch in not_allowed_multiple:
        if counter.get(ch, 0) > 1:
            return True

    return False


def is_valid_subtractive_notation(curr_ch, next_ch):

    # (key, valuers) pairs, where key can only be followed by one of its values
    # to make a subtractive form.

    valid_subtract_dict = dict([('I', ['V', 'X']),
                           ('X', ['L', 'C']),
                           ('C', ['D', 'M'])])

    return next_ch in valid_subtract_dict.get(curr_ch, [])


def roman_numeral_from_string(numeral):

    # check if string empty, or has invalid chars.
    if not numeral or not has_valid_roman_chars(numeral):
        return None

    # D, L or V are only allowed once.
    if has_multiple_DLV(numeral):
        return None

    answer = 0
    i, length = 0, len(numeral)

    # value of current char or pair.
    current_value = 0

    while i < length:
        # current char
        ch1 = numeral[i].upper()
        val1 = int_value(ch1)

        # to check it subtractive pair.
        if i+1 < length:

            # next char
            ch2 = numeral[i+1].upper()
            val2 = int_value(ch2)

            # if both current and next char are same.
            # then check for third char
            # to avoid invalid IIV or XXL type strings.
            if ch2 == ch1:
                if i+2 < length:
                    ch3 = numeral[i+2].upper()
                    val3 = int_value(ch3)
                    if val3 > val2:
                        return None

            # not subtractive form.
            if val1 >= val2:
                current_val = val1
                i = i + 1
            # check if valid subtractive form.
            elif is_valid_subtractive_notation(ch1, ch2):
                current_val = val2 - val1
                i = i + 2
            # not valid subtractive.
            else:
                return None

        # last char.
        else:
            current_val = val1
            i = i + 1

        # add current value to the answer.
        answer = answer + current_val

    return answer


def main():

    in_st = input("Enter the roman numeral string(1-3999): ").strip()

    answer = roman_numeral_from_string(in_st) 

    if answer:
        print("Integer value: ", answer)
    else:
        print("Invalid roman numeral.")


if __name__ == "__main__":
    main()
