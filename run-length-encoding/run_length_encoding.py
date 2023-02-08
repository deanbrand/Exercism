def decode(string):
    if len(string) == 0:
        return ""
    decoded = ""
    it = enumerate(string)
    for index, char in it:
        if char.isdigit():
            if string[index + 1].isdigit():
                decoded += string[index + 2] * (int(string[index:index + 2]))
                [next(it, None) for _ in range(2)]
            else:
                decoded += string[index + 1] * (int(char) - 1)
        else:
            decoded += char
    return decoded


def encode(string):
    if len(string) == 0:
        return ""
    count = 1
    encoded = ""
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            if count != 1:
                encoded += str(count) + string[i - 1]
            else:
                encoded += string[i - 1]
            count = 1
    if count != 1:
        encoded += str(count) + string[i]
    else:
        encoded += string[i]
    return encoded
