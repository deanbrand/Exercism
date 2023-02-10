ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]


def rows(letter):
    diamond = []
    let_len = ALPHABET.index(letter)
    for ind, let in enumerate(ALPHABET[:let_len + 1]):
        diamond.append((" " * (let_len - ind) + let + " " * ind)[:-1] + " " * ind + let + " " * (let_len - ind))
    for ind, let in enumerate(ALPHABET[:let_len][::-1]):
        diamond.append(
            (" " * (ind + 1) + let + " " * (let_len - ind - 1))[:-1] + " " * (let_len - ind - 1) + let + " " * (
                    ind + 1))
    return diamond
