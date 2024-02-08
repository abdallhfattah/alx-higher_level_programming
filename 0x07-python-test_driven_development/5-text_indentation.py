#!/usr/bin/python3
"""text_indentation method."""


def text_indentation(text):
    """Print two new lines after each '.', '?', and ':'.

    Args:
        text: (string) The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev = ' '
    for character in text:
        if character != '.' and character != '?' and character != ':':
            if prev == ' ' and character == ' ':
                continue
            else:
                print(character, end='')
                prev = character
                if character == '\n':
                    prev = ' '
        else:
            print(character, end='\n\n')
            prev = ' '
