def is_armstrong_number(number):
    string = str(number)
    n_digits = len(string)
    armstrong = 0

    for digit in string:
        armstrong += int(digit) ** n_digits

    return bool(armstrong == number)
