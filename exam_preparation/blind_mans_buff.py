n, m = [int(x) for x in input().split()]
matrix = []
for row in range(n):
    matrix.append(input().split())

BLIND_MAN = "B"
OBSTACLE = "O"
OPPONENT = "P"
EMPTY = "-"
DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
blind_man_position = []
for row in range(n):
    for col in range(m):
        if matrix[row][col] == BLIND_MAN:
            blind_man_position = [row, col]

command = input()
while command != "Finish":
    next_row = mouse_position[0] + DIRECTIONS[command][0]
    next_col = mouse_position[1] + DIRECTIONS[command][1]

    command = input()