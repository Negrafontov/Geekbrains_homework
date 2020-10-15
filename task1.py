class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        matrix_to_str = '\n'.join(map(str, self.list_of_lists))
        return matrix_to_str

    def __len__(self):
        return len(self.list_of_lists)

    def __getitem__(self, item):
        return self.list_of_lists[item]

    def __add__(self, other):
        result = [[self[i][j] + other[i][j] for j in range(len(self[0]))] for i in range(len(self))]
        new_matrix = Matrix(result)
        return new_matrix


list_of_lists1 = [[1, 2, 4], [3, 4, 5], [2, 5, 8]]
list_of_lists2 = [[3, 4, 5], [4, 6, 8], [9, 4, 7]]
list_of_lists3 = [[6, 9], [4, 3], [5, 7]]
list_of_lists4 = [[0, 1], [9, 4], [6, 2]]

matrix1 = Matrix(list_of_lists1)
matrix2 = Matrix(list_of_lists2)
matrix3 = Matrix(list_of_lists3)
matrix4 = Matrix(list_of_lists4)

print(matrix1)
print(matrix1 + matrix2)