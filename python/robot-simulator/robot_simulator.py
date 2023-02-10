# Globals for the directions
# Change the values as you see fit
EAST = {"dir": "EAST", "Ax": 1, "Ay": 0, "L": "NORTH", "R": "SOUTH"}
NORTH = {"dir": "NORTH", "Ax": 0, "Ay": 1, "L": "WEST", "R": "EAST"}
WEST = {"dir": "WEST", "Ax": -1, "Ay": 0, "L": "SOUTH", "R": "NORTH"}
SOUTH = {"dir": "SOUTH", "Ax": 0, "Ay": -1, "L": "EAST", "R": "WEST"}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)

    def move(self, instructions):
        instructions_list = list(instructions)
        for inst in instructions_list:
            self.direction = globals()[self.direction[inst]] if inst != "A" else self.direction
            if inst == "A":
                self.x_pos += self.direction["Ax"]
                self.y_pos += self.direction["Ay"]
                continue
        self.coordinates = (self.x_pos, self.y_pos)
