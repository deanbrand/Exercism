def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")

    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]

    new_row = [1]
    result = rows(row_count - 1)
    last_row = result[-1]

    for i in range(len(last_row) - 1):
        num = last_row[i] + last_row[i + 1]
        new_row.append(num)

    new_row.append(1)
    result.append(new_row)

    return result
