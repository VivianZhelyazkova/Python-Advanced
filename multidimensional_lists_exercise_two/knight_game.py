n = int(input())

matrix = [[x for x in input().split()] for _ in range(n)]

KNIGHT = "K"
EMPTY = "0"

knights_to_be_removed = 0


def find_knight_position(some_matrix):
    knights_positions = []
    for row_index, row in enumerate(some_matrix):
        for col_index, char in enumerate(row):
            if char == KNIGHT:
                knights_positions.append([row_index, col_index])
    return knights_positions


def find_knight_attacks(position, some_matrix):
    knights_attacks = []
    row, col = position
    knights_attacks.append([row - 2, col + 1])
    knights_attacks.append([row - 1, col + 2])
    knights_attacks.append([row + 1, col + 2])
    knights_attacks.append([row + 2, col + 1])
    knights_attacks.append([row + 2, col - 1])
    knights_attacks.append([row + 1, col - 2])
    knights_attacks.append([row - 1, col - 2])
    knights_attacks.append([row - 2, col - 1])
    return knights_attacks


knights_positions = find_knight_position(matrix)
