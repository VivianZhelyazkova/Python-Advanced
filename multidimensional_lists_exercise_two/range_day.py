n = 5
matrix = [[x for x in input().split()] for _ in range(n)]
number_of_commands = int(input())

SHOOTER = "A"
TARGET = "x"
EMPTY = "."


def move(dire, step):
    moves = {
        "right": [0, 0 + steps],
        "left": [0, 0 - steps],
        "up": [0 - steps, 0],
        "down": [0 + steps, 0]
    }
    return moves[dire]


shooter_position = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == SHOOTER:
            shooter_position = [row, col]

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
    elif "shoot" in command:
        cmd, direction = command.split()
        row, col = shooter_position
        if direction == "right":
            shooting_range = range(row, n)


    print(next_move)
    print(next_row)
    print(next_col)
