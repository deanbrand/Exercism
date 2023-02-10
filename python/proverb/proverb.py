def proverb(*args, qualifier=None):
    if len(args) == 0:
        return []
    proverb_out = []
    for ind, item in enumerate(args[:-1]):
        proverb_out.append(f"For want of a {args[ind]} the {args[ind + 1]} was lost.")
    if qualifier is not None:
        proverb_out.append(f"And all for the want of a {qualifier} {args[0]}.")
    else:
        proverb_out.append(f"And all for the want of a {args[0]}.")
    return proverb_out
