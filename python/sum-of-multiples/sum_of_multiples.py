def sum_of_multiples(limit, multiples):
    return sum(number for number in range(limit) if any(factor and not number % factor for factor in multiples))
