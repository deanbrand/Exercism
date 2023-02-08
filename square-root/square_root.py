def square_root(number):
    # Newton-Raphson Method

    r = number
    precision = 10 ** (-10)

    while abs(number - r * r) > precision:
        r = (r + number / r) / 2

    return r // 1
