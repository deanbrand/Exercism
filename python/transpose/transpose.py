PADDING = "*"


def transpose(lines):
    lines = lines.split("\n")
    matrix_size = max([len(row) for row in lines])
    lines = map(lambda row: row.ljust(matrix_size, PADDING), lines)
    lines = map(lambda row: "".join(list(row)), zip(*lines))
    lines = map(lambda row: row.rstrip(PADDING).replace(PADDING, " "), lines)
    return "\n".join(lines)
