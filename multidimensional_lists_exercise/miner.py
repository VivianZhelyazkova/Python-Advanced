n = int(input())

commands = input().split()

matrix = [[x for x in input().split()] for _ in range(n)]

def get_new_position(str,row,col):
    coms = {
        "left": [row,col-1],
        "right": [row,col +1],
        "up": [row -1,col],
        "down": [row +1,col]
        }



miner_col, miner_row = 0, 0

for index, row in enumerate(matrix):
    if "s" in row:
        miner_col = row.index("s")
        miner_row = index

for command in commands:


[print(*row) for row in matrix]
