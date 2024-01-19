import re

rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]

command = input()
regex = r"^swap( \d+){4}$"
regex = re.compile(regex)

while command != "END":
    match = regex.match(command)
    if match:
        cmd, row_1, col_1, row_2, col_2 = command.split()
        row_1 = int(row_1)
        col_1 = int(col_1)
        row_2 = int(row_2)
        col_2 = int(col_2)
        if row_1 < rows and row_2 < rows and col_1 < cols and col_2 < cols:
            matrix[row_1][col_1],matrix[row_2][col_2] = matrix[row_2][col_2],matrix[row_1][col_1]
            [print(*row) for row in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()
