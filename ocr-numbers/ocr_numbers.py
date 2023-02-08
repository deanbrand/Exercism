NUMBER_STRINGS = {" _ | ||_|": "0", "     |  |": "1", " _  _||_ ": "2", " _  _| _|": "3", "   |_|  |": "4",
                  " _ |_  _|": "5",
                  " _ |_ |_|": "6", " _   |  |": "7", " _ |_||_|": "8", " _ |_| _|": "9"}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    splits = [input_grid[i:i + 4] for i in range(0, len(input_grid), 4)]
    num_list = ""

    for split in splits:
        numbers = len(split[0]) // 3
        matrix = []
        num_collapsed = ""
        for line in split:
            matrix.append([line[i:i + 3] for i in range(0, len(line), 3)])
        for i in range(numbers):
            for col in range(3):
                num_collapsed += matrix[col][i]
            if num_collapsed in NUMBER_STRINGS:
                num_list += NUMBER_STRINGS[num_collapsed]
            else:
                num_list += "?"
            num_collapsed = ""

        num_list += "," if len(splits) > 1 else ""
    return num_list.strip(",")
