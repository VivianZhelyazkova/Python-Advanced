import sys

rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

result = {}
max_value = -sys.maxsize


def making_submatrix(x, y, matrix):
    length = 3
    submatrix = []
    current_sum = 0
    for i in range(y, y + length):
        current_row = []
        for j in range(x, x + length):
            current_row.append(matrix[i][j])
            current_sum += matrix[i][j]
        submatrix.append(current_row)
    current_result = {current_sum: submatrix}
    return current_result


for y in range(rows - 2):
    for x in range(cols - 2):
        current_result = making_submatrix(x, y, matrix)
        current_max = int(list(current_result.keys())[0])
        if current_max > max_value:
            max_value = current_max
            result = current_result

print(f"Sum = {max_value}")

for sum, matrix in current_result.items():
    for row in matrix:
        print(*row, sep=" ")
