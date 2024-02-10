n = int(input())
commands = input().split(", ")
matrix = []
for row in range(n):
    matrix.append(list(input()))

DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

SQUIRREL = "s"
NUT = "h"
EMPTY = "*"
TRAP = "t"

squirrel_position = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == SQUIRREL:
            squirrel_position = [row, col]

collected_nuts = 0
is_alive = True

for command in commands:
    next_row = squirrel_position[0] + DIRECTIONS[command][0]
    next_col = squirrel_position[1] + DIRECTIONS[command][1]

    if next_row not in range(n) or next_col not in range(n):
        print("The squirrel is out of the field.")
        is_alive = False
        break

    next_position = matrix[next_row][next_col]

    if next_position == NUT:
        collected_nuts += 1
        matrix[next_row][next_col] = EMPTY
        if collected_nuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif next_position == TRAP:
        print("Unfortunately, the squirrel stepped on a trap...")
        is_alive = False
        break

    squirrel_position = [next_row, next_col]

if collected_nuts < 3 and is_alive:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_nuts}")

