class Cell:
    def __init__(self, cell_number):
        self.cell_number = int(cell_number)

    def __add__(self, other):
        new_value = self.cell_number + other.cell_number
        new_cell = Cell(new_value)
        return new_cell

    def __sub__(self, other):
        if self.cell_number <= other.cell_number:
            return 'Ошибка! {} меньше, чем {}'.format(self.cell_number, other.cell_number)
        else:
            return self.cell_number - other.cell_number

    def __mul__(self, other):
        new_value = self.cell_number * other.cell_number
        new_cell = Cell(new_value)
        return new_cell

    def __truediv__(self, other):
        new_value = self.cell_number // other.cell_number
        new_cell = Cell(new_value)
        return new_cell

    def make_order(self, cells_in_row):
        number_of_rows = self.cell_number // cells_in_row
        leftover = self.cell_number % cells_in_row
        cell_string = ''
        for cell in range(number_of_rows):
            cell_string = cell_string + ('*' * cells_in_row + '\n')
        if leftover != 0:
            cell_string = cell_string + '*' * leftover
            return cell_string
        else:
            return cell_string


cell1 = Cell(8)
cell2 = Cell(9)
cell3 = Cell(7)

print((cell1 + cell2).cell_number)
print(cell1 - cell2)
print(cell1 - cell3)
print((cell1 * cell2).cell_number)
print((cell1 / cell3).cell_number)
print(cell1.make_order(3))