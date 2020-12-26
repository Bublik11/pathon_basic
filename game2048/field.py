import random


class Field(object):
    def __init__(self, cells_in_row=4):
        self.cell_in_row = cells_in_row
        self.matrix = []
        temp_row = [0] * cells_in_row
        for _ in range(cells_in_row):
            self.matrix.append(temp_row.copy())

    def print_field(self):
        """Напечатать матрицу"""

        for row in self.matrix:
            for cell in row:
                print(f"{cell}", end='\t')
            print()

    def empty_cells(self):
        result = []
        for ind_r, row in enumerate(self.matrix):
            for ind_c, cell in enumerate(row):
                if not cell:
                    result.append([ind_r, ind_c])
        return tuple(result)

    def add_rand_value(self):
        empty_cells = self.empty_cells()
        if len(empty_cells):
            rand = random.randint(0, len(empty_cells) - 1)
            row = empty_cells[rand][0]
            column = empty_cells[rand][1]
            self.matrix[row][column] = 2
        else:
            self.end_game()

    def end_game(self):
        pass

    def check_moves(self):
        self.end_game()
        pass

    def move_right(self):
        c_cell = self.cell_in_row
        for row in self.matrix:
            c = c_cell - 2
            while c >= 0:
                if c < c_cell - 1:
                    if row[c] == row[c + 1]:
                        row[c + 1], row[c] = row[c]*2, 0
                        c -= 1
                    elif (row[c]) and (not row[c + 1]):
                        row[c + 1], row[c] = row[c], 0
                        c += 1
                    else:
                        c -= 1
                else:
                    c -= 1

    def move_left(self):
        c_cell = self.cell_in_row
        for row in self.matrix:
            c = 1
            while c <= c_cell - 1:
                if c > 0:
                    if row[c] == row[c - 1]:
                        row[c - 1], row[c] = row[c]*2, 0
                        c += 1
                    elif (row[c]) and (not row[c - 1]):
                        row[c - 1], row[c] = row[c], 0
                        c -= 1
                    else:
                        c += 1
                else:
                    c += 1
