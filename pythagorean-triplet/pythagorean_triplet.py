# a**2 + b**2 = c**2
# a + b + c = N <->
# a**2 + b**2 = c**2
# a + b = N - c
# Solving system of equations for a and b
# D = sqrt(c**2 - N**2 + 2*N*c)
# a = (N - c - D)/2
# b = (N - c + D)/2
# D is real for c > N * (sqrt(2) - 1)
# And c < N/2 from the problem statement
import math


def triplets_with_sum(number):
    n = float(number)
    triplets = []
    for c in range(int(n / 2) - 1, int((math.sqrt(2) - 1) * n), -1):
        d = math.sqrt(c ** 2 - n ** 2 + 2 * n * c)
        if d == int(d):
            triplets.append([int((n - c - d) / 2), int((n - c + d) / 2), c])
    return triplets
