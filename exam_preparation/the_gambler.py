n = int(input())
matrix = []
for row in range(n):
    matrix.append(list(input()))


def move_gambler(old_pos, new_pos):
    new_row, new_col = new_pos
    matrix[old_pos[0]][old_pos[1]] = EMPTY
    matrix[new_row][new_col] = GAMBLER
    return [new_row, new_col]


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

money = 100

gambler_position = []

for row in range(n):
    for col in range(n):
        if matrix[row][col] == GAMBLER:
            gambler_position = [row, col]

command = input()

while command != 'end':
    next_row = gambler_position[0] + DIRECTIONS[command][0]
    next_col = gambler_position[1] + DIRECTIONS[command][1]

    if next_row not in range(n) or next_col not in range(n):
        print("Game over! You lost everything!")
        exit()
    next_position = matrix[next_row][next_col]
    gambler_position = move_gambler(gambler_position, [next_row, next_col])

    if next_position == WIN:
        money += 100

    elif next_position == PENALTY:
        money -= 200
        if money <= 0:
            print("Game over! You lost everything!")
            exit()
    elif next_position == JACKPOT:
        money += 100000
        print(f"You win the Jackpot!")
        break

    command = input()

print(f"End of the game. Total amount: {money}$")

[print(''.join(row)) for row in matrix]