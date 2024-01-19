rows = int(input())

matrix = [[int() for x in input().split(", ")] for row in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for y in range(rows):
    for x in range(y, y + 1):
        primary_diagonal.append(matrix[x][y])

for x in range(rows):
    secondary_diagonal.append(matrix[x][rows-1-x])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
