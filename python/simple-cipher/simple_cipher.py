from random import randint


class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = self.generate_key(101)
        self.key = key.lower()
        self.shift_key = [ord(key_char) - ord("a") for key_char in key]

    def encode(self, text):
        encoded = ""
        i = 0
        for letter in text:
            shift = ord(letter) + self.shift_key[i % len(self.shift_key)]
            if shift > ord("z"):
                shift = shift - (ord("z") - ord("a") + 1)
            encoded_letter = chr(shift)
            encoded += encoded_letter
            i += 1
        return encoded

    def decode(self, text):
        decoded = ""
        i = 0
        for letter in text:
            shift = ord(letter) - self.shift_key[i % len(self.shift_key)]
            if shift < ord("a"):
                shift = shift + (ord("z") - ord("a") + 1)
            decoded_letter = chr(shift)
            decoded += decoded_letter
            i += 1
        return decoded

    @staticmethod
    def generate_key(length):
        new_key = ""
        for l in range(length):
            new_key += chr(randint(ord("a"), ord("z")))
        return new_key
