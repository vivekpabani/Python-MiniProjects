#!/usr/bin/env python

"""
Description:
Take roman numeral as a string and return it as an integer.
If the string is not valid return None.

"""
__author__ = "vivek"



import sys


def read_currency_codes(source_file):
    """
    :param source_file: path of the file with currency codes.  
    :returns: dictionary with (key, value) as (code, currency name) 
    """

    code_dict = dict()

    with open(filename) as f:
        data = f.readlines()

        for line in data:
            terms = line.strip().split(',')
            code, currency = terms[0].strip(), terms[1].strip()
            code_dict[code] = currency            

    return code_dict


def get_inputs():
    """
    Get user inputs.

    :returns: from_code, to_code, amount
    """ 
    try: 
        from_code = input("Enter the from_currency code : ").upper() 
        to_code = input("Enter the to_currency code : ").upper() 
        amount = int(input("Enter the amount : ").strip())
    except:
        print("Invalid input(s). Try again.")
        sys.exit(1)

    return from_code, to_code, amount 
