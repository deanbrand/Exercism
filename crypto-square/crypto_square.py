import string
import math

PADDING = "*"


def cipher_text(plain_text):
    normalized_text = plain_text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    l = len(normalized_text)
    if l == 0:
        return ""
    c = math.ceil(math.sqrt(len(normalized_text)))
    r = math.floor(math.sqrt(len(normalized_text)))
    rows = [normalized_text[i:i + c] for i in range(0, l, c)]
    rows[-1] += " " * (c - len(rows[-1]))
    return transpose("\n".join(rows))


def transpose(lines):
    lines = lines.split("\n")
    matrix_size = max([len(row) for row in lines])
    lines = map(lambda row: row.ljust(matrix_size, PADDING), lines)
    lines = map(lambda row: "".join(list(row)), zip(*lines))
    lines = map(lambda row: row.rstrip(PADDING).replace(PADDING, " "), lines)
    return " ".join(lines)
