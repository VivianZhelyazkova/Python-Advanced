rows = int(input())
symbol = input()

matrix = []

for row in range(rows):
    matrix.append(list(input()))

is_found = False

for y in range(rows):
    for x in range(rows):
        if matrix[y][x] == symbol:
            print(f"({y}, {x})")
            break
