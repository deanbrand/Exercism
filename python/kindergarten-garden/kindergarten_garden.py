STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
            "Larry"]
PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            self.students = STUDENTS
        else:
            self.students = students
            self.students.sort()
        self.first_row, self.second_row = diagram.split("\n")
        self.first_row_split = [self.first_row[i:i + 2] for i in range(0, len(self.first_row), 2)]
        self.second_row_split = [self.second_row[i:i + 2] for i in range(0, len(self.second_row), 2)]

    def plants(self, name):
        plant_list = list("".join([self.first_row_split[self.students.index(name)],
                                   self.second_row_split[self.students.index(name)]]))
        plant_names_list = [PLANTS[plant] for plant in plant_list]
        return plant_names_list
