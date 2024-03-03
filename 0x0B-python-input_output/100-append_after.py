#!/usr/bin/python3
"""Defines a new_text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_text after each line containing a given string in a file."""
    new_text = ""
    with open(filename) as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w") as f:
        f.write(new_text)
