
OPS = {
    "plus": "__add__", "minus": "__sub__",
    "multiplied by": "__mul__", "divided by": "__truediv__"
}


def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question:
        raise ValueError("syntax error")
    if question.isdigit():
        return int(question)
    isOP = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            isOP = True
    if not isOP:
        raise ValueError("unknown operation")
    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.values():
                raise ValueError("syntax error")
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except:
            raise ValueError("syntax error")
    return ret[0]
