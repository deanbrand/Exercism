def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = []
    for lst in lists:
        new_list += lst
    return new_list


def filter(function, list):
    new_list = []
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    func_list = []
    for item in list:
        func_list.append(function(item))
    return func_list


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(item, initial)
    return initial


def reverse(list):
    reversed_list = []
    for item in list:
        reversed_list = [item] + reversed_list
    return reversed_list
