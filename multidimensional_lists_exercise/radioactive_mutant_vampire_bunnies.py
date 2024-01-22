from collections import deque

row_count, col_count = [int(x) for x in input().split()]
matrix = [[x for x in input()] for x in range(row_count)]
commands = deque(input())

PLAYER = "P"
BUNNY = "B"
EMPTY = "."

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"


def get_player_position(some_matrix):
    player_position = []
    for row_index, row in enumerate(some_matrix):
        if PLAYER in row:
            player_row = row_index
            player_col = row.index(PLAYER)
            player_position.append(player_row)
            player_position.append(player_col)
    return player_position


def get_new_position(cmd, position, is_for_bunny=False):
    row, col = position
    commands_map = {
        LEFT: [row, col - 1],
        RIGHT: [row, col + 1],
        UP: [row - 1, col],
        DOWN: [row + 1, col]
    }
    if is_for_bunny:
        return commands_map[cmd] if is_within_matrix(position) else position
    return commands_map[cmd]


def is_within_matrix(position):
    row, col = position
    return row < row_count and col < col_count and row >= 0 and col >= 0


def get_bunnies_positions(some_matrix):
    bunnies_positions = []
    for row_index, row in enumerate(some_matrix):
        for col_index, col in enumerate(row):
            if col == BUNNY:
                bunnies_positions.append([row_index, col_index])
    return bunnies_positions


def multiply_bunnies():
    bunny_positions = get_bunnies_positions(matrix)
    for coordinates in bunny_positions:
        top_bunny = get_new_position(UP, coordinates, True)
        bot_bunny = get_new_position(DOWN, coordinates, True)
        left_bunny = get_new_position(LEFT, coordinates, True)
        right_bunny = get_new_position(RIGHT, coordinates, True)
        matrix[top_bunny[0]][top_bunny[1]] = BUNNY
        matrix[bot_bunny[0]][bot_bunny[1]] = BUNNY
        matrix[left_bunny[0]][left_bunny[1]] = BUNNY
        matrix[right_bunny[0]][right_bunny[1]] = BUNNY
        print(top_bunny)


is_alive = True
has_escaped = False

while commands and is_alive and not has_escaped:
    command = commands.popleft()
    player_position = get_player_position(matrix)
    new_position = get_new_position(command, player_position)
    has_escaped = not is_within_matrix(new_position)
    matrix[player_position[0]][player_position[1]] = EMPTY

    if not has_escaped:
        if matrix[new_position[0]][new_position[1]] != BUNNY:
            matrix[new_position[0]][new_position[1]] = PLAYER

        else:
            is_alive = False

    multiply_bunnies()

[print(*row) for row in matrix]
