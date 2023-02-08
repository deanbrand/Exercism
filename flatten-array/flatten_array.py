def flatten(iterable):
    flattened = []
    for entry in iterable:
        if entry != None:
            flattened += [entry] if not isinstance(
                entry, list) else flatten(entry)
    return flattened
