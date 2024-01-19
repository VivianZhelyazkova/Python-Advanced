rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for x in range(rows):
    primary_diagonal.append(matrix[x][x])

for x in range(rows):
    secondary_diagonal.append(matrix[x][rows-1-x])

diff = abs(sum(primary_diagonal)-sum(secondary_diagonal))
print(diff)