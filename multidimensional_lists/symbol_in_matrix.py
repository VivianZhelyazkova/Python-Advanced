rows = int(input())
matrix = []

for row in range(rows):
    matrix.append(list(input()))

symbol = input()

is_found = False

for y in range(rows):
    for x in range(rows):
        if matrix[y][x] == symbol:
            print(f"({y}, {x})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
