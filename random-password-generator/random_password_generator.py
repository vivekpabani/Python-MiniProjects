#!/usr/bin/env python 

"""
Description:
Take roman numeral as a string and return it as an integer.
If the string is not valid return None.

"""
__author__ = "vivek"



import sys
import getopt
import string
import random

def get_arguments():

    arguments = sys.argv[1:]
    plen, uppercase, numbers = 8, True, True  

    try:
        opts, args = getopt.getopt(arguments,"hl:",["help", "nouppercase", "nonumbers"])
    except getopt.GetoptError:
        print("Please run with correct arguments.")
        print("Run Instruction : python3 <script.py> [-h] [-l <password_length>] [--nouppercase] [--nonumbers]")
        sys.exit(1) 

    for opt, arg in opts:
        if opt == '-h':
            print("Run Instruction : python3 <script.py> [-h] [-l <password_length>] [--nouppercase] [--nonumbers]")
            sys.exit(1)
        elif opt == "-l":
            try:
                plen = int(arg)
            except:
                # invalid length value. default taken.
                pass 
        elif opt == "--nouppercase":
            uppercase = False
        elif opt == "--nonumbers":
            numbers = False 

    return plen, uppercase, numbers


def main():

    plen, uppercase, numbers = get_arguments()
    print(plen, uppercase, numbers)


if __name__ == "__main__":
    main()
