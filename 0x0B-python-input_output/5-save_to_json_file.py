#!/usr/bin/python3
"""
5-save_to-json_file: save to json file()
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using json rep
    Args:
    my_obj (object):object to be serialized.
    filename (str):name of the file where the string is to be strored.
    """
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)
