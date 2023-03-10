def largest_product(series, size):
    if size == 0:
        return 1

    if size > len(series):
        raise ValueError("span must be smaller than string length")

    if size < 1:
        raise ValueError("span must not be negative")

    if not series.isnumeric():
        raise ValueError("digits input must only contain digits")

    largest = 0
    for i in range(len(series) - size + 1):
        prod_string = series[i: i + size]
        prod = 1
        for num in prod_string:
            prod *= int(num)
        if prod > largest:
            largest = prod
    return largest
