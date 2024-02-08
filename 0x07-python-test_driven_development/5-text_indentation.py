#!/usr/bin/python3
"""text_indentation method."""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start =  True
    for character in text:
        if character != '.' and character != '?' and character != ':':
            if start and character == ' ':
                start = False
            else:
                print(character, end='')
        else:
            print(character, end='\n\n')
            start = True
