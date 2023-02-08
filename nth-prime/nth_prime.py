def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    count = 0
    i = 2
    while count < number:
        for j in range(2, int(i / 2) + 1):
            if (i % j) == 0:
                break
        else:
            count += 1
        i += 1
    return i - 1
