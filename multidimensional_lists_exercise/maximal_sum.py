rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append(input().split())

result = float("-inf")
values = []

for y in range(rows - 2):
    for x in range(cols - 2):
        top_one = matrix[y][x]
        top_two = matrix[y][x + 1]
        top_three = matrix[y][x + 2]
        bottom_one = matrix[y + 1][x]
        bottom_two = matrix[y + 1][x + 1]
        bottom_three = matrix[y + 1][x + 2]
        current_result = top_one + top_
        if current_result > result:
            result = current_result
            values = [[top_left, top_right], [bottom_left, bottom_right]]