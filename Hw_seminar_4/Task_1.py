# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6]]
def trans_Matrix(matrix: list[list]) -> (list[list]):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

print(matrix)
print(trans_Matrix(matrix))
