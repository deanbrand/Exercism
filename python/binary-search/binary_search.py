def find(search_list, value):
    found = False
    original = search_list

    while not found:
        if len(search_list) < 1:
            raise ValueError("value not in array")
        mid = len(search_list) // 2
        if value not in search_list:
            raise ValueError("value not in array")
        if value == search_list[mid]:
            return original.index(search_list[mid])
        if value < search_list[mid]:
            search_list = search_list[:mid]
            continue
        if value > search_list[mid]:
            search_list = search_list[mid:]
            continue
