n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))


def move_submarine(old_pos, new_pos):
    new_row, new_col = new_pos
    matrix[old_pos[0]][old_pos[1]] = EMPTY
    matrix[new_row][new_col] = SUBMARINE
    return [new_row, new_col]


DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
SUBMARINE = "S"
MINE = "*"
EMPTY = "-"
CRUISER = "C"
submarine_position = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == SUBMARINE:
            submarine_position = [row, col]
hits = 0
cruisers = 3

while True:
    command = input()
    next_row = submarine_position[0] + DIRECTIONS[command][0]
    next_col = submarine_position[1] + DIRECTIONS[command][1]
    next_position = matrix[next_row][next_col]
    submarine_position = move_submarine(submarine_position, [next_row, next_col])
    if next_position == MINE:
        hits += 1
        if hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!")
            break
    elif next_position == CRUISER:
        cruisers -= 1
        if not cruisers:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

[print("".join(row)) for row in matrix]
