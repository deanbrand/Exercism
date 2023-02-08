def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if not isbn[-1].isdigit() and isbn[-1] != 'X':
        return False
    if not isbn[:-1].isdigit():
        return False
    total = 0
    if isbn[-1] == 'X':
        total = 10
    for scalar, digit in enumerate(isbn):
        try:
            total += (10 - scalar) * int(digit)
        except:
            pass
    return total % 11 == 0
