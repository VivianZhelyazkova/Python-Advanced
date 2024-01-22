from collections import deque

row, col = [int(x) for x in input().split()]
matrix = [[x for x in input()] for x in range(row)]
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


def get_new_position(cmd, position):
    row, col = position
    commands_map = {
        LEFT: [row, col - 1],
        RIGHT: [row, col + 1],
        UP: [row - 1, col],
        DOWN: [row + 1, col]
    }
    return commands_map[cmd]


def is_within_matrix(position, x, y):
    row, col = position
    return row == x or col == y or row < 0 or col < 0


def get_bunnies_positions(some_matrix):
    bunnies_positions = []
    for row_index, row in enumerate(some_matrix):
        for col_index, col in enumerate(row):
            if col == BUNNY:
                bunnies_positions.append([row_index, col_index])
    return bunnies_positions


def multiply_bunnies(bunny_positions,some_matrix):
    for coordinates in bunny_positions:
        row, col = coordinates
        


is_alive = True
has_escaped = False

while commands and is_alive and not has_escaped:
    command = commands.popleft()
    player_position = get_player_position(matrix)
    new_position = get_new_position(command, player_position)
    has_escaped = is_within_matrix(new_position, row, col)

print(matrix)
