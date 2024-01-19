rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = 0
secondary_diagonal = 0

for x in range(rows):
    primary_diagonal += matrix[x][x]
    secondary_diagonal += matrix[x][rows - 1 - x]

diff = abs(primary_diagonal - secondary_diagonal)
print(diff)
