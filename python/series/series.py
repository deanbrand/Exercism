def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    series_num = len(series) - (length - 1)
    series_list = []

    for sub in range(series_num):
        series_list.append(series[sub:sub + length])

    return series_list
