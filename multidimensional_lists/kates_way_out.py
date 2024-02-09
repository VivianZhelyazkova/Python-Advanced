n = int(input())
KATE = "k"
EMPTY = " "
WALL = "#"
PATH = "*"
matrix = [[x for x in input()] for _ in range(n)]

positions = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0]
}


def is_valid(pos, some_matrix):
    curr_row, curr_col = pos
    return curr_row in range(n) and curr_col in range(len(some_matrix[curr_row]))


def moving(pos, some_matrix, steps):
    current_row, current_col = pos
    if not is_valid(pos, some_matrix):
        return True
    if some_matrix[current_row][current_col] == WALL:
        return False

    for k, v in positions.items():
        new_row, new_col = v
        new_row += current_row
        new_col += current_col
        if is_valid([new_row, new_col], some_matrix):
            if some_matrix[new_row][new_col] == EMPTY:
                matrix[current_row][current_col] = PATH
                if moving([new_row, new_col], some_matrix, steps + 1):
                    return True
        else:
            print(f"Kate got out in {steps} moves")
            return True
    return False


kate_position = []

for row in range(n):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "k":
            kate_position = [row, col]

if not moving(kate_position, matrix, 1):
    print("Kate cannot get out")
