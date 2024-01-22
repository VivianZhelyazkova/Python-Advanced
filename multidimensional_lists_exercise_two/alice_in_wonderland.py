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
    next_coordinates = positions[command]
    row, col = next_coordinates
    next_position = [alice_position[0] + row, alice_position[1] + col]
    new_row, new_col = next_position

    if new_row in range(n) and new_col in range(n) and matrix[new_row][new_col] != HOLE:

        if matrix[new_row][new_col] != EMPTY and matrix[new_row][new_col] != PATH:
            bags += int(matrix[new_row][new_col])
        path_row, path_col = alice_position
        matrix[path_row][path_col] = PATH
        alice_position = next_position

    # elif new_row in range(n) and new_col in range(n) and matrix[new_row][new_col] == HOLE:
    #     matrix[new_row][new_col] = PATH
    #     is_within = False

    else:
        is_within = False

    

if bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row, sep=" ") for row in matrix]
