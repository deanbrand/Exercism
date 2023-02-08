class School:
    def __init__(self):
        self.names = []
        self.tf = []
        self.students = {}

    def add_student(self, name, grade):
        if name in self.names:
            self.tf.append(False)
        else:
            self.names.append(name)
            self.tf.append(True)
            if grade in self.students:
                self.students[grade].append(name)
                self.students[grade].sort()
            else:
                self.students[grade] = [name]
        self.students = dict(sorted(self.students.items()))

    def roster(self):
        roster_list = [student for student in self.students.values()]
        return [item for sublist in roster_list for item in sublist]

    def grade(self, grade_number):
        if grade_number in self.students.keys():
            return self.students[grade_number]
        return []

    def added(self):
        return self.tf
