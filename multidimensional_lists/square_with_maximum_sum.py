rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for x in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

result = float("-inf")
values = []

for y in range(rows - 1):

    for x in range(cols - 1):
        top_left = matrix[y][x]
        top_right = matrix[y][x + 1]
        bottom_left = matrix[y + 1][x]
        bottom_right = matrix[y + 1][x + 1]
        current_result = top_left + top_right + bottom_left + bottom_right
        if current_result > result:
            result = current_result
            values = [[top_left, top_right], [bottom_left, bottom_right]]

print(*values[0], sep=" ")
print(*values[1], sep=" ")
print(result)
