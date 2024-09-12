#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text to be processed

    Raises:
    TypeError: If text is not a string

    Returns:
    None: This function prints the formatted text, it doesn't return anything
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in [".", "?", ":"]:
            print("\n")

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            i -= 1
        i += 1
