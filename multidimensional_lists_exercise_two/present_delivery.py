presents = int(input())
n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]

SANTA = "S"
NAUGHTY = "X"
NICE = "V"
COOKIES = "C"
EMPTY = "-"


def get_new_position(direction, position):
    current_row, current_col = position
    moves = {
        "right": [current_row, current_col + 1],
        "left": [current_row, current_col - 1],
        "up": [current_row - 1, current_col],
        "down": [current_row + 1, current_col]
    }
    temp_row, temp_col = moves[direction]
    if temp_row in range(n) and temp_col in range(n):
        return moves[direction]
    return position


def move(s_position, x, y, some_matrix):
    some_matrix[s_position[0]][s_position[1]] = EMPTY
    some_matrix[x][y] = SANTA
    new_santa_position = [x, y]
    return new_santa_position


santa_position = []
total_nice_kids = 0
nice_kids = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == SANTA:
            santa_position = [row, col]
        if matrix[row][col] == NICE:
            nice_kids += 1
total_nice_kids = nice_kids
command = input()

while command != "Christmas morning":
    next_move = get_new_position(command, santa_position)
    new_row, new_col = next_move
    if matrix[new_row][new_col] == NAUGHTY or matrix[new_row][new_col] == EMPTY:
        santa_position = move(santa_position, new_row, new_col, matrix)
    elif matrix[new_row][new_col] == NICE:
        santa_position = move(santa_position, new_row, new_col, matrix)
        presents -= 1
        nice_kids -= 1
    elif matrix[new_row][new_col] == COOKIES:
        santa_position = move(santa_position, new_row, new_col, matrix)
        kids = []
        kids.append(get_new_position("left", santa_position))
        kids.append(get_new_position("right", santa_position))
        kids.append(get_new_position("up", santa_position))
        kids.append(get_new_position("down", santa_position))

        for kid in kids:

            if matrix[kid[0]][kid[1]] != EMPTY and matrix[kid[0]][kid[1]] != COOKIES:
                if matrix[kid[0]][kid[1]] == NICE and presents:
                    nice_kids -= 1
                if presents:
                    presents -= 1
                matrix[kid[0]][kid[1]] = EMPTY

    if presents:
        command = input()
    else:
        break

if not presents and nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if nice_kids:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids - nice_kids} happy nice kid/s.")
