n, m = [int(x) for x in input().split(",")]

matrix = []
for row in range(n):
    matrix.append(list(input()))

DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
MOUSE = "M"
CHEESE = "C"
EMPTY = "*"
WALL = "@"
TRAP = "T"

mouse_position = []
for row in range(n):
    for col in range(m):
        if matrix[row][col] == MOUSE:
            mouse_position = [row, col]

command = input()

while command != "danger":
    next_row = mouse_position[0] + DIRECTIONS[command][0]
    next_col = mouse_position[1] + DIRECTIONS[command][1]

    if next_row not in range(n) or next_col not in range(m):
        print("No more cheese for tonight!")
        break

    next_position = matrix[next_row][next_col]

    if 




    command = input()