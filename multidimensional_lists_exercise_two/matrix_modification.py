n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input()


def are_coords_valid(x, y, some_matrix):
    return x in range(n) and y in range(n)


while command != "END":
    cmd, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if are_coords_valid(row, col, matrix):
        if cmd == "Add":
            matrix[row][col] += value
        elif cmd == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

[print(*row, sep=" ") for row in matrix]
