n, m = [int(x) for x in input().split(', ')]
matrix = []
for row in range(n):
    matrix.append(input().split())

SANTA = "Y"
DECORATIONS = "D"
GIFTS = "G"
COOKIES = "C"
EMPTY = "."
PATH = "x"
DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
collected_items = {
    DECORATIONS: 0,
    GIFTS: 0,
    COOKIES: 0
}
santa_position = []
total_items = 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] == SANTA:
            santa_position = [row, col]
        elif matrix[row][col] != EMPTY:
            total_items += 1
command = input()
all_items_collected = False

while command != "End":
    direction, steps = command.split("-")
    for step in range(int(steps)):
        matrix[santa_position[0]][santa_position[1]] = PATH
        next_row = santa_position[0] + DIRECTIONS[direction][0]
        next_col = santa_position[1] + DIRECTIONS[direction][1]
        if next_row < 0:
            next_row = n - 1
        elif next_row == n:
            next_row = 0
        if next_col < 0:
            next_col = m - 1
        elif next_col == m:
            next_col = 0
        current_position = matrix[next_row][next_col]
        if current_position != EMPTY and current_position != PATH and current_position != SANTA:
            collected_items[current_position] += 1
        matrix[next_row][next_col] = PATH
        santa_position = [next_row, next_col]
        if sum(collected_items.values()) == total_items:
            print("Merry Christmas!")
            all_items_collected = True
            break
    matrix[santa_position[0]][santa_position[1]] = SANTA
    if all_items_collected:
        break
    command = input()

print("You've collected:")
print(f"- {collected_items[DECORATIONS]} Christmas decorations")
print(f"- {collected_items[GIFTS]} Gifts")
print(f"- {collected_items[COOKIES]} Cookies")
[print(*row) for row in matrix]
