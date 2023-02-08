DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]
GIFTS = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]


def recite(start_verse, end_verse):
    song = []
    for verse in range(start_verse, end_verse + 1):
        song.append(f'On the {DAYS[verse - 1]} day of Christmas'
                    ' my true love gave to me: '
                    f'{", ".join(GIFTS[verse - 1:0:-1])}'
                    f'{", and " if verse > 1 else ""}'
                    f'{GIFTS[0]}.')
    return song
