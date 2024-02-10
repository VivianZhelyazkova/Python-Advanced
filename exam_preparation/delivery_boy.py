n, m = [int(x) for x in input().split()]

matrix = []
for row in range(n):
    matrix.append(list(input()))

DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

BOY = "B"
ADDRESS = "A"
OBSTACLE = "*"
PIZZA = "P"
EMPTY = "-"
READY = "R"
PATH = "."

boy_position = []

for row in range(n):
    for col in range(m):
        if matrix[row][col] == BOY:
            boy_position = [row, col]

starting_position = boy_position

while True:
    command = input()

    next_row = boy_position[0] + DIRECTIONS[command][0]
    next_col = boy_position[1] + DIRECTIONS[command][1]

    if next_row in range(n) and next_col in range(m):

        next_position = matrix[next_row][next_col]
        if next_position != OBSTACLE:
            boy_position = [next_row, next_col]

        if next_position == PIZZA:
            matrix[next_row][next_col] = READY
            print("Pizza is collected. 10 minutes for delivery.")

        elif next_position == ADDRESS:
            matrix[next_row][next_col] = PIZZA
            print("Pizza is delivered on time! Next order...")
            break

        elif next_position == EMPTY:
            matrix[next_row][next_col] = PATH

    else:
        matrix[starting_position[0]][starting_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

[print("".join(row)) for row in matrix]
