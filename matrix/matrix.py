class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.lines = matrix_string.split('\n')
        self.matx = [list(map(lambda x: int(x), rw.split(" "))) for rw in self.lines]

    def row(self, index):
        return self.matx[index - 1]

    def column(self, index):
        return [self.matx[col][index - 1] for col in range(len(self.matx))]
