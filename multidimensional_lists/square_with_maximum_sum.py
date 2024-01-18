rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for x in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

result = 0
values = []

for y in range(cols):

    for x in range(rows):
        if x + 1 == rows - 1 or y + 1 == cols - 1:
            break
        top_left = matrix[y][x]
        top_right = matrix[y][x + 1]
        bottom_left = matrix[y + 1][x]
        bottom_right = matrix[y + 1][x + 1]
        current_result = top_left + top_right + bottom_left + bottom_right
        if current_result > result:
            result = current_result
            values.append(top_left)
            values.append(top_right)
            values.append(bottom_left)
            values.append(bottom_right)

print(result)
print(values)
