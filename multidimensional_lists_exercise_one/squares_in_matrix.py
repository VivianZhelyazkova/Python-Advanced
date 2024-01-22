rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append(input().split())

squares = 0

for y in range(rows - 1):
    for x in range(cols - 1):
        top_left = matrix[y][x]
        top_right = matrix[y][x + 1]
        bottom_left = matrix[y + 1][x]
        bottom_right = matrix[y + 1][x + 1]
        if top_left == top_right and bottom_left == bottom_right and top_right == bottom_right:
            squares += 1

print(squares)