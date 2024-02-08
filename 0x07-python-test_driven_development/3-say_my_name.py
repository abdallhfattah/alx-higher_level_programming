#!/usr/bin/python3
# 3-say_my_name.py
"""say_my_name method."""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints your name in certain formate
    Args:
        first_name : (str) first name
        last_name : (str) last name (optional)
    Raise:
        TypeError : if either of the args is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
