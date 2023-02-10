from collections import Counter

FACE_CARD_NUMS = {"J": 11, "Q": 12, "K": 13, "A": 14}


def best_hands(hands):
    """
    Given a list of hands, return the best poker hand.
    """
    hand_ranks = [classify(hand) for hand in hands]
    best = max(hand_ranks)
    return [hands[i] for i in range(len(hands)) if hand_ranks[i] == best]


def get_matches(hand):
    """
    Give matched numbers to assess hand type and rank
    """
    values = [card[:-1] for card in hand.split()]
    nums = sorted([int(FACE_CARD_NUMS.get(num, num)) for num in values],
                  reverse=True
                  )
    return Counter(nums).most_common(5)


def classify(hand):
    """
    Given a hand, return tuple with the type of hand and the card values.
    """

    # Create list of tuples of card value and number of cards of that value.
    # Unpack and zip into a tuple of card values and a tuple of match numbers.
    values, counts = zip(*get_matches(hand))
    # Treat ace as 1 in a low straight.
    values = (5, 4, 3, 2, 1) if values == (14, 5, 4, 3, 2) else values
    flush = len(set([c[-1] for c in hand.split()])) == 1
    straight = len(counts) == 5 and min(values) + 4 == max(values)

    hand_code = (
        8 if straight and flush else  # Straight flush
        7 if counts[0] == 4 else  # 4-of-a-kind
        6 if counts == (3, 2) else  # Full house
        5 if flush else  # Flush
        4 if straight else  # Straight
        3 if counts[0] == 3 else  # 3-of-a-kind
        2 if counts[:2] == (2, 2) else  # Two pair
        1 if counts[0] == 2 else  # One pair
        0  # High card
    )
    return hand_code, *values
