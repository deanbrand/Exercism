def factors(value):
    factor_list = []
    divisor = 2
    remaining = value

    while remaining > 1:
        if remaining % divisor == 0:
            factor_list.append(divisor)
            remaining = remaining // divisor
        else:
            divisor += 1
    return factor_list
