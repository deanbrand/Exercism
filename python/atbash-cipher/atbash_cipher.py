PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'


def encode(plain_text):
    encoded = ''
    grouping = 0
    plain_text = plain_text.lower().replace(' ', '').replace('.', '').replace(',', '')
    for letter in plain_text:
        if letter in PLAIN:
            encoded += CIPHER[PLAIN.rfind(letter)]
        else:
            encoded += letter
        grouping += 1
        if grouping % 5 == 0:
            encoded += ' '
    return encoded.strip()


def decode(ciphered_text):
    decoded = ''
    for letter in ciphered_text:
        if letter in CIPHER:
            decoded += PLAIN[CIPHER.rfind(letter)]
        else:
            decoded += letter
    return decoded.replace(' ', '')
