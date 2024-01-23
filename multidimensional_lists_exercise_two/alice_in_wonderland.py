n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]

ALICE = "A"
HOLE = "R"
EMPTY = "."
PATH = "*"

positions = {"up": [-1, 0],
             "down": [1, 0],
             "left": [0, -1],
             "right": [0, 1],
             }

alice_position = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == ALICE:
            alice_position = [row, col]

bags = 0
is_within = True

while bags < 10 and is_within:
    command = input()
    next_position = [alice_position[0] + positions[command][0], alice_position[1] + positions[command][1]]
    new_row, new_col = next_position

    if new_row in range(n) and new_col in range(n):
        if matrix[new_row][new_col] == HOLE:
            is_within = False

        elif matrix[new_row][new_col] != EMPTY and matrix[new_row][new_col] != PATH:
            bags += int(matrix[new_row][new_col])
        path_row, path_col = alice_position
        matrix[path_row][path_col] = PATH
        alice_position = next_position

    else:
        is_within = False

if alice_position[0] in range(n) and alice_position[1] in range(n):
    matrix[alice_position[0]][alice_position[1]] = PATH

if bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row, sep=" ") for row in matrix]
