n, m = [int(x) for x in input().split(",")]

matrix = []
for row in range(n):
    matrix.append(list(input()))


def move_mouse(old_pos, new_pos):
    new_row, new_col = new_pos
    matrix[old_pos[0]][old_pos[1]] = EMPTY
    matrix[new_row][new_col] = MOUSE
    return [new_row, new_col]


DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
MOUSE = "M"
CHEESE = "C"
EMPTY = "*"
WALL = "@"
TRAP = "T"

mouse_position = []
total_cheese = 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] == MOUSE:
            mouse_position = [row, col]
        elif matrix[row][col] == CHEESE:
            total_cheese += 1

command = input()
shadow_got_the_mouse = False

while command != "danger":
    next_row = mouse_position[0] + DIRECTIONS[command][0]
    next_col = mouse_position[1] + DIRECTIONS[command][1]

    if next_row not in range(n) or next_col not in range(m):
        print("No more cheese for tonight!")
        shadow_got_the_mouse = True
        break

    next_position = matrix[next_row][next_col]

    if next_position != WALL:
        mouse_position = move_mouse(mouse_position, [next_row, next_col])

    if next_position == CHEESE:
        total_cheese -= 1
        if total_cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif next_position == TRAP:
        shadow_got_the_mouse = True
        print("Mouse is trapped!")
        break

    command = input()

if total_cheese and not shadow_got_the_mouse:
    print("Mouse will come back later!")

[print(''.join(row)) for row in matrix]
