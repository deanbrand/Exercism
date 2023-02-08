import re


def abbreviate(words):
    return ''.join(letter[0].upper() for letter in re.findall(r"[a-zA-Z']+", words))
