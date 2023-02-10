NUMBERS = ['No', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']


def recite(start, take=1):
    buffer = ""
    song = []

    for verses in range(take):
        num = NUMBERS[start - verses]
        nxt = NUMBERS[start - verses - 1]
        if num == "Two":
            song.append(f"{num} green bottles hanging on the wall,")
            song.append(f"{num} green bottles hanging on the wall,")
            song.append("And if one green bottle should accidentally fall,")
            song.append(f"There'll be {nxt.lower()} green bottle hanging on the wall.")
        elif num == "One":
            song.append(f"{num} green bottle hanging on the wall,")
            song.append(f"{num} green bottle hanging on the wall,")
            song.append("And if one green bottle should accidentally fall,")
            song.append(f"There'll be {nxt.lower()} green bottles hanging on the wall.")
        else:
            song.append(f"{num} green bottles hanging on the wall,")
            song.append(f"{num} green bottles hanging on the wall,")
            song.append("And if one green bottle should accidentally fall,")
            song.append(f"There'll be {nxt.lower()} green bottles hanging on the wall.")
        if take > 1:
            song.append(buffer)
    if take > 1:
        song.pop()

    return song
