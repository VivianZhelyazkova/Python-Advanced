from functools import reduce

n = int(input())

commands = input().split()

matrix = [[x for x in input().split()] for _ in range(n)]
COAL = "c"
END = "e"
EMPTY = "*"
MINER = "s"


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


def coal_left(some_matrix):
    flatten = reduce(lambda a, b: a + b, some_matrix)
    coal = flatten.count(COAL)
    return coal


miner_position = []
total_coal = 0

for index, row in enumerate(matrix):
    if MINER in row:
        miner_col = row.index(MINER)
        miner_row = index
        miner_position.append(miner_row)
        miner_position.append(miner_col)

for command in commands:
    next_position = get_new_position(command, miner_position)
    miner_position = next_position
    row, col = miner_position

    if matrix[row][col] == COAL:
        total_coal += 1
        matrix[row][col] = EMPTY

    elif matrix[row][col] == END:
        print(f"Game over! ({row}, {col})")
        exit()
row, col = miner_position
remaining_coal = coal_left(matrix)

if remaining_coal == 0:
    print(f"You collected all coal! ({row}, {col})")
else:
    print(f"{remaining_coal} pieces of coal left. ({row}, {col})")
