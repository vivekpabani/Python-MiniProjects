#!/usr/bin/env python

"""
Description:
Take roman numeral as a string and return it as an integer.
If the string is not valid return None.

"""
__author__ = "vivek"



import sys
import requests


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


def get_convertion_rate(from_code, to_code, code_dict):
    """
    Get the conversion rate using input codes.
    if invalid codes, return -1
    if can't find conversion, return 0

    :param from_code: code of from currency
    :param to_code: code of to currency
    :param code_dict: dictionary with currency codes.
    :returns: if found, conversion rate. if invalid codes, return -1. if can't find conversion, return -1 
    """"
    codes = code_dict.keys()

    if from_code not in codes or to_code not in codes:
        return -1

    url = "http://rate-exchange.appspot.com/currency?from=" + from_code + "&to=" + to_code 
    response = requests.get(url) 
    
    if response.status_code != 200:
        return 0

    rate = float(response.json()['rate']) 

    return rate
