n, m = [int(x) for x in input().split()]
matrix = []
for row in range(n):
    matrix.append(input().split())


def move_blind_man(old_pos, new_pos):
    new_row, new_col = new_pos
    matrix[old_pos[0]][old_pos[1]] = EMPTY
    matrix[new_row][new_col] = BLIND_MAN
    return [new_row, new_col]


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
touched_opponents = 0
moves = 0
while command != "Finish":
    next_row = blind_man_position[0] + DIRECTIONS[command][0]
    next_col = blind_man_position[1] + DIRECTIONS[command][1]
    if next_row in range(n) and next_col in range(m):
        next_position = matrix[next_row][next_col]
        if next_position != OBSTACLE:
            blind_man_position = move_blind_man(blind_man_position, [next_row, next_col])
            moves += 1
            if next_position == OPPONENT:
                touched_opponents += 1
                if touched_opponents == 3:
                    break
    command = input()

print(f"Game over!\n"
      f"Touched opponents: {touched_opponents} Moves made: {moves}")
