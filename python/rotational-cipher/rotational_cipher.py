CHARS = "abcdefghijklmnopqrstuvwxyz"


def rotate(text, key):
    new_chars = CHARS[key:] + CHARS[:key]
    trans = str.maketrans(CHARS + CHARS.upper(), new_chars + new_chars.upper())
    return text.translate(trans)
