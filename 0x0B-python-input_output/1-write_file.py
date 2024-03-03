#!/usr/bin/python3
"""Defines a function that writes string to file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
