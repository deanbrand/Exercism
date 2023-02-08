def equilateral(sides):
    if isTriangle(sides) == False or positive(sides) == False:
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    if isTriangle(sides) == False or positive(sides) == False:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return True
    return False


def scalene(sides):
    if isTriangle(sides) == False or positive(sides) == False:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return False
    return True


def isTriangle(sides):
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False


def positive(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0:
        return True
    return False
