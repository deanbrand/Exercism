import string
import re


class PhoneNumber:
    def __init__(self, number):
        if re.findall("[!@#$%^&*={}]", number):
            raise ValueError("punctuations not permitted")
        num = number.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
        if len(num) < 10:
            raise ValueError("incorrect number of digits")
        if len(num) > 11:
            raise ValueError("more than 11 digits")
        if len(num) == 11 and num[0] != "1":
            raise ValueError("11 digits must start with 1")
        if num[-10:-1][3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if num[-10:-1][3] == "1":
            raise ValueError("exchange code cannot start with one")
        if num[-10:-1][0] == "0":
            raise ValueError("area code cannot start with zero")
        if num[-10:-1][0] == "1":
            raise ValueError("area code cannot start with one")
        if re.findall("[a-zA-Z]", num):
            raise ValueError("letters not permitted")
        self.number = num[-10:]
        self.area_code = self.number[:3]

    def pretty(self):
        return "(" + self.area_code + ")-" + self.number[3:6] + "-" + self.number[6:]
