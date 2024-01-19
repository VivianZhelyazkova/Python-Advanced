rows, cols = [int(x) for x in input().split()]

matrix = []
a = ord("a")

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append((chr(a + row) + chr(a + col + row) + chr(a + row)))

[print(*row, sep=" ") for row in matrix]
