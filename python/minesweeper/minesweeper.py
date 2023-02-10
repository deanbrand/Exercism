def annotate(minefield):
    if not minefield:
        return []

    st = [list(line) for line in minefield]

    allowed = {" ", "*"}

    chars = [set(st[i]) for i in range(len(st))]

    for i in chars:
        if not i.issubset(allowed):
            raise ValueError("The board is invalid with current input.")

    lens = []

    for line in st:
        lens.append(len(line))

    if len(set(lens)) != 1:
        raise ValueError("The board is invalid with current input.")

    m = len(st)
    n = len(st[0])

    neighbours = find_neighbours_matrix(st)
    joined = []

    for i in range(m):
        for j in range(n):
            if st[i][j] == "*":
                continue
            if count(neighbours[i][j], "*") == 0:
                continue
            st[i][j] = str(count(neighbours[i][j], "*"))
        joined.append("".join(st[i]))

    return joined


def find_neighbours_matrix(matrix):
    neighbours_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            neighbours = []
            # check left
            if j > 0:
                neighbours.append(matrix[i][j - 1])
            # check right
            if j < len(matrix[i]) - 1:
                neighbours.append(matrix[i][j + 1])
            # check top
            if i > 0:
                neighbours.append(matrix[i - 1][j])
            # check bottom
            if i < len(matrix) - 1:
                neighbours.append(matrix[i + 1][j])
            # check top-left
            if i > 0 and j > 0:
                neighbours.append(matrix[i - 1][j - 1])
            # check top-right
            if i > 0 and j < len(matrix[i]) - 1:
                neighbours.append(matrix[i - 1][j + 1])
            # check bottom-left
            if i < len(matrix) - 1 and j > 0:
                neighbours.append(matrix[i + 1][j - 1])
            # check bottom-right
            if i < len(matrix) - 1 and j < len(matrix[i]) - 1:
                neighbours.append(matrix[i + 1][j + 1])
            row.append(neighbours)
        neighbours_matrix.append(row)
    return neighbours_matrix


def count(charlist, target):
    num = 0
    for char in charlist:
        if char == target:
            num += 1
    return num
