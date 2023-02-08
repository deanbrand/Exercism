def value(colors):
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

    resistor = str(colours.index(colors[0])) + str(colours.index(colors[1]))
    return int(resistor)
