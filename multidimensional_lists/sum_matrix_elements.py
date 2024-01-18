matrix = []

rows, cols = [int(x) for x in input().split(',')]

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

total_sum = 0

for row in matrix:
    total_sum += sum(row)

print(total_sum)
print(matrix)
