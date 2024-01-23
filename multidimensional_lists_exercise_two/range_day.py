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
        if direction == "right":
            col_range = range(col, n)
        elif direction == "left":
            col_range = range(col, -1, -1)
        elif direction == "up":
            row_range = range(row, -1, -1)
        elif direction == "down":
            row_range = range(row, n)

        if

    print(next_move)
    print(next_row)
    print(next_col)
