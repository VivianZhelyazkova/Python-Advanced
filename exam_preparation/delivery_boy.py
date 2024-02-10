n, m = [int(x) for x in input().split()]

matrix = []
for row in range(n):
    matrix.append(list(input()))


def move_boy(old_pos, new_pos):
    new_row, new_col = new_pos
    matrix[old_pos[0]][old_pos[1]] = EMPTY
    matrix[new_row][new_col] = BOY
    return [new_row, new_col]


DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

BOY = "B"
ADDRESS = "A"
OBSTACLE = "*"
PIZZA = "P"
EMPTY = "-"

boy_position = []

for row in range(n):
    for col in range(m):
        if matrix[row][col] == BOY:
            boy_position = [row, col]


while True:
    command = input()
    
    next_row = boy_position[0] + DIRECTIONS[command][0]
    next_col = boy_position[1] + DIRECTIONS[command][1]