#!/usr/bin/python3
#Author: Vincent Ondeng

def uppercase(str):
    """Print a string in Uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
