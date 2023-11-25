#!/usr/bin/python3
# 5-text_indentation.py
"""Creates a function for indenting text."""


def text_indentation(text):
    """
Display text with double line breaks following each '.', '?', and ':'.
Parameters:
- text (string): The text to be displayed.
Raises:
- TypeError: If the input 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
