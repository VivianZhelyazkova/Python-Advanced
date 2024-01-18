rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(num) for num in input().split()])


result = 0

for x in range(rows):
    result += matrix[x][x]

print(result)

