import itertools


def is_rect(points, strings):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = sorted(list(points))

    if x1 != x2 or x3 != x4 or y1 != y3 or y2 != y4:
        return False

    if strings[y1][x1 + 1:x3].count(' ') > 0:
        return False

    if strings[y2][x1 + 1:x3].count(' ') > 0:
        return False

    for y in range(y1 + 1, y2):
        if strings[y][x1] in [' ', '-']:
            return False

        if strings[y][x3] in [' ', '-']:
            return False

    return True


def rectangles(strings):
    count = 0
    plus = []

    for y, string in enumerate(strings):
        for x, c in enumerate(string):
            if c == '+': plus += [(x, y)]

    for points in list(itertools.combinations(plus, 4)):
        count += is_rect(points, strings)

    return count
