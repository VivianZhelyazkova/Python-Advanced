n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))

DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
GAMBLER = "G"
WIN = "W"
PENALTY = "P"
JACKPOT = "J"
EMPTY = "-"
MONEY = 100

gambler_position = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == GAMBLER:
            gambler_position = [row, col]

command = input()

while command != 'end':
    
    next_row = gambler_position[0] + DIRECTIONS[command][0]
    next_col = gambler_position[1] + DIRECTIONS[command][1]

    command = input()
