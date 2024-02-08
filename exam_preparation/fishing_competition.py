n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))

SAILOR = "S"
WHIRLPOOL = "W"
EMPTY = "-"
QUOTA = 20

DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
fish_collected = 0

sailor_position = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == SAILOR:
            sailor_position = [row, col]
            matrix[row][col] = EMPTY

command = input()

while command != "collect the nets":

    next_row = sailor_position[0] + DIRECTIONS[command][0]
    next_col = sailor_position[1] + DIRECTIONS[command][1]

    if next_row not in range(n) or next_col not in range(n):
        if next_row < 0:
            next_row = n-1
        elif next_row == n:
            next_row = 0
        elif next_col < 0:
            next_col = n-1
        elif next_col == n:
            next_col = 0

    if matrix[next_row][next_col] == WHIRLPOOL:
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{next_row},{next_col}]"
        )
        exit()
    elif matrix[next_row][next_col].isdigit():
        fish_collected += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = EMPTY

    sailor_position = [next_row, next_col]

    command = input()

matrix[sailor_position[0]][sailor_position[1]] = SAILOR

if fish_collected < QUOTA:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {QUOTA - fish_collected} tons of fish more.")
else:
    print("Success! You managed to reach the quota!")

if fish_collected:
    print(f"Amount of fish caught: {fish_collected} tons.")

[print("".join(row)) for row in matrix]
