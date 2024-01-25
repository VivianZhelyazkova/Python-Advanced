import sys

sys.setrecursionlimit(3000)

n = int(input())
KATE = "k"
EMPTY = " "
WALL = "#"

matrix = [[x for x in input()] for _ in range(n)]

positions = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0]
}


def moving(pos, some_matrix):
    current_row, current_col = pos
    if current_row not in range(n) or current_col not in range(len(some_matrix[current_row])):
        print("whatever")
        return True
    if some_matrix[current_row][current_col] == WALL:
        return False

    left_row, left_col = positions["left"]
    if moving([left_row + current_row, left_col + current_col], some_matrix):

        return True
    right_row, right_col = positions["right"]
    if moving([right_row + current_row, right_col + current_col], some_matrix):

        return True
    up_row, up_col = positions["up"]
    if moving([up_row + current_row, up_col + current_col], some_matrix):

        return True
    down_row, down_col = positions["down"]
    if moving([down_row + current_row, down_col + current_col], some_matrix):

        return True
    return False


kate_position = []

for row in range(n):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "k":
            kate_position = [row, col]

print(moving(kate_position, matrix))

[print(row) for row in matrix]
