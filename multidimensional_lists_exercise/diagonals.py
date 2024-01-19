rows = int(input())
cols = rows
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(',')])

primary_diagonal = []
secondary_diagonal = []

for y in range(rows):
    for x in range(y, y + 1):
        primary_diagonal.append(matrix[x][y])

for y in range(rows):
    for x in range(y, y - 1, -1):
        secondary_diagonal.append(matrix[y][x])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)})")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)})")
