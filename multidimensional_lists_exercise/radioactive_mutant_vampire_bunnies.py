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


def escaped(position, x, y):
    row, col = position
    return row == x or col == y or row < 0 or col < 0
   



is_alive = True
has_escaped = False

while commands and is_alive and not has_escaped:
    command = commands.popleft()

print(matrix)
