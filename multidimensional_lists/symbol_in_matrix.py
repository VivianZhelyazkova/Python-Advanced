rows = int(input())
matrix = []

for row in range(rows):
    matrix.append(list(input()))

symbol = input()
#
# is_found = False

for y in range(rows):
    for x in range(rows):
        if matrix[y][x] == symbol:
            print(f"({y}, {x})")
            # is_found = True
            # break
            exit()
    # if is_found:
    #     break

print(f"{symbol} does not occur in the matrix")
