n = 6
matrix = []
for row in range(n):
    matrix.append(input().split())
starting_pos = [int(x) for x in input() if x.isdigit()]

DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
EMPTY = "."

command = input()
while command != "Stop":
    cmd, *info = command.split(", ")
    direction = info[0]
    next_row = starting_pos[0] + DIRECTIONS[direction][0]
    next_col = starting_pos[1] + DIRECTIONS[direction][1]
    next_position = matrix[next_row][next_col]
    starting_pos = [next_row, next_col]
    if cmd == "Create":
        value = info[1]
        if next_position == EMPTY:
            matrix[next_row][next_col] = value
    elif cmd == "Update":
        value = info[1]
        if next_position != EMPTY:
            matrix[next_row][next_col] = value
    elif cmd == "Delete":
        if next_position != EMPTY:
            matrix[next_row][next_col] = EMPTY
    elif cmd == "Read":
        if next_position != EMPTY:
            print(matrix[next_row][next_col])
    command = input()

[print(" ".join(row)) for row in matrix]