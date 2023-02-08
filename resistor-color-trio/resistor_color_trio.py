def label(colors):
    colours = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

    resistor = str(colours.index(colors[0])) + str(colours.index(colors[1])) + ("0" * colours.index(colors[2]))
    if int(resistor) >= 1000:
        resistor = str(int(resistor) // 1000) + " kiloohms"
    else:
        resistor += " ohms"
    return resistor
