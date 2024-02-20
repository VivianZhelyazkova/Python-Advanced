n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))

JET = "J"
ENEMY = "E"
REPAIR = "R"
EMPTY = "-"
DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
enemy_count = 4
armor = 300

jet_position = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == JET:
            jet_position = [row, col]

while enemy_count and armor:
    command = input()
    next_row = jet_position[0] + DIRECTIONS[command][0]
    next_col = jet_position[1] + DIRECTIONS[command][1]
    next_position = matrix[next_row][next_col]
    matrix[next_row][next_col] = JET
    matrix[jet_position[0]][jet_position[1]] = EMPTY
    jet_position = [next_row, next_col]

    if next_position == "E":
        enemy_count -= 1
        armor -= 100
        if enemy_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        if armor == 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
            break
    elif next_position == REPAIR:
        armor = 300

[print("".join(row)) for row in matrix]