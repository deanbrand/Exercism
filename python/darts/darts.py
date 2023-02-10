def score(x, y):
    points = 0

    radius = x ** 2 + y ** 2

    if radius <= 100:
        points = 1
    if radius <= 25:
        points = 5
    if radius <= 1:
        points = 10

    return points
