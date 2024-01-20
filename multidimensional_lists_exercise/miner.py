n = int(input())

commands = input().split()

matrix = [[x for x in input().split()] for _ in range(n)]


def get_new_position(cmd, position):
    row, col = position
    coms = {
        "left": [row, col - 1],
        "right": [row, col + 1],
        "up": [row - 1, col],
        "down": [row + 1, col]
    }
    return coms[cmd] if is_position_valid(coms[cmd]) else position


def is_position_valid(position):
    row, col = position
    if row < 0 or col < 0:
        return False
    if row > n - 1 or col > n - 1:
        return False
    return True


miner_position = []

for index, row in enumerate(matrix):
    if "s" in row:
        miner_col = row.index("s")
        miner_row = index
        miner_position.append(miner_row)
        miner_position.append(miner_col)

for command in commands:

[print(*row) for row in matrix]
