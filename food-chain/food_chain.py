from functools import reduce


def recite(start_verse, end_verse):
    return reduce(
        lambda a, b: a + [""] + b,
        [recite_verse(i) for i in range(start_verse + 1, end_verse + 1)],
        recite_verse(start_verse),
    )


def recite_verse(verse):
    rhymes = [
        ("fly", "fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
        ("spider", "spider that{}".format(action := " wriggled and jiggled and tickled inside her"), f"It{action}."),
        ("bird", "bird", "How absurd to swallow a bird!"),
        ("cat", "cat", "Imagine that, to swallow a cat!"),
        ("dog", "dog", "What a hog, to swallow a dog!"),
        ("goat", "goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "cow", "I don't know how she swallowed a cow!"),
        ("horse", "horse", "She's dead, of course!"),
    ]
    lines = [
        f"I know an old lady who swallowed a {rhymes[verse - 1][0]}.",
        rhymes[verse - 1][2],
    ]
    if 1 < verse < 8:
        lines += [
                     f"She swallowed the {rhymes[i][0]} to catch the {rhymes[i - 1][1]}."
                     for i in range(verse - 1, 0, -1)
                 ] + [rhymes[0][2]]
    return lines
