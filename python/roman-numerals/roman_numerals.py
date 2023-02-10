NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
LETTERS = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


def roman(number):
    numeral = ""
    while number > 0:
        for ind, val in enumerate(NUMBERS):
            if number >= val:
                numeral += LETTERS[ind]
                number -= val
                break
    return numeral
