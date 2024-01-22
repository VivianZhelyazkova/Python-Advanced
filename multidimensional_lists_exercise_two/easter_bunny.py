n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]

BUNNY = "B"
TRAP = "X"

bunny_position = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == BUNNY:
            bunny_position = [row, col]

max_sum = float("-inf")
best_position = ""
best_route = []

positions = {(-1, 0): "up",
             (+1, 0): "down",
             (0, -1): "left",
             (0, +1): "right",
             }

for coordinates, direction in positions.items():
    current_sum = 0
    row, col = coordinates
    new_row = bunny_position[0] + row
    new_col = bunny_position[1] + col
    current_route = []
    while True:
        if new_row in range(n) and new_col in range(n):
            if matrix[new_row][new_col] != TRAP:
                current_sum += int(matrix[new_row][new_col])
                current_route.append([new_row, new_col])
            else:
                break
        else:
            break
        new_row += row
        new_col += col
    if current_sum >= max_sum:
        max_sum = current_sum
        best_position = direction
        best_route = current_route

print(best_position)
[print(row) for row in best_route]
print(max_sum)


