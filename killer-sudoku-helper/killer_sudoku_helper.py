from itertools import combinations as combos


def combinations(target, size, exclude):
    nums = list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(exclude))
    return [list(combo) for combo in combos(nums, size) if
            sum(combo) == target]
