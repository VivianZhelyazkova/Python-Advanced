n = 5
matrix = [[x for x in input().split()] for _ in range(n)]
number_of_commands = int(input())

SHOOTER = "A"
TARGET = "x"
EMPTY = "."


def move(dire, step):
    moves = {
        "right": [0, step],
        "left": [0, -step],
        "up": [-step, 0],
        "down": [step, 0]
    }
    return moves[dire]


shooter_position = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == SHOOTER:
            shooter_position = [row, col]

targets_shot = []

for _ in range(number_of_commands):

    command = input()

    if "move" in command:
        cmd, direction, steps = command.split()
        steps = int(steps)
        next_move = move(direction, steps)
        next_row = next_move[0] + shooter_position[0]
        next_col = next_move[1] + shooter_position[1]

        if next_row in range(n) and next_col in range(n):
            if matrix[next_row][next_col] == EMPTY:
                matrix[shooter_position[0]][shooter_position[1]] = EMPTY
                matrix[next_row][next_col] = SHOOTER
                shooter_position = [next_row, next_col]
    elif "shoot" in command:
        cmd, direction = command.split()
        row, col = shooter_position

        target_found = False

        while row in range(n) and col in range(n) and not target_found:
            next_move = move(direction, 1)
            row = next_move[0] + row
            col = next_move[1] + col
            if row in range(n) and col in range(n):
                if matrix[row][col] == TARGET:
                    matrix[row][col] = EMPTY
                    targets_shot.append([row,col])
                    target_found = True

targets_left = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == TARGET:
            targets_left += 1

if targets_left:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {len(targets_shot)} targets hit.")

for target in targets_shot:
    print(target)