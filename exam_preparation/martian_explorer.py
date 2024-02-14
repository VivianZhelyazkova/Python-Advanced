from collections import deque

n = 6
matrix = []
for row in range(n):
    matrix.append(input().split())

ROVER = "E"
WATER = "W"
METAL = "M"
CONCRETE = "C"
ROCK = "R"
EMPTY = "-"
DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
DEPOSIT_NAMES_MAP = {
    WATER: "Water",
    METAL: "Metal",
    CONCRETE: "Concrete"
}
gathered_deposits = {
    WATER: 0,
    METAL: 0,
    CONCRETE: 0
}
commands = deque(input().split(", "))
rover_position = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == ROVER:
            rover_position = [row, col]

while commands:
    command = commands.popleft()
    next_row = rover_position[0] + DIRECTIONS[command][0]
    next_col = rover_position[1] + DIRECTIONS[command][1]

    if next_row not in range(n) or next_col not in range(n):
        if next_col < 0:
            next_col = n - 1
        elif next_col >= n:
            next_col = 0
        if next_row < 0:
            next_row = n - 1
        elif next_row >= n:
            next_row = 0
    next_position = matrix[next_row][next_col]
    if next_position != ROCK and next_position != EMPTY:
        gathered_deposits[next_position] += 1
        print(f"{DEPOSIT_NAMES_MAP[next_position]} deposit found at ({next_row}, {next_col})")
    elif next_position == ROCK:
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    rover_position = [next_row, next_col]

if all(gathered_deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")