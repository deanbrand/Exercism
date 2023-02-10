VOWELS = "aeiou"


def translate(text: str):
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word: str):
    return rearrange_word(word) + "ay"


def rearrange_word(word: str):
    if word[0] in VOWELS or word[:2] in ("xr", "yt") or (word[0] == "y" and word[1] not in VOWELS):
        return word
    elif word[:2] == "qu":
        return word[2:] + word[:2]
    else:
        return rearrange_word(word[1:] + word[0])
