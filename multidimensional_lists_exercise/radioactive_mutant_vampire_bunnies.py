row, col = [int(x) for x in input().split()]
matrix = [[x for x in input()] for x in range(row)]
commands = [x for x in input()]

PLAYER = "P"
BUNNY = "B"
EMPTY = "."

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"

is_alive = True
has_escaped = False

while commands and is_alive and not has_escaped:

    



print(matrix)