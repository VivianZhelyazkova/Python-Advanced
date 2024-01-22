n = int(input())

matrix = [[x for x in input()] for _ in range(n)]

KNIGHT = "K"
EMPTY = "0"


def find_knight_attacks(position):
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


knights_removed = 0

while True:
    max_attacks = 0
    max_knight_attacks_pos = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == KNIGHT:
                attacks = 0
                for attack in find_knight_attacks([row, col]):
                    attack_row, attack_col = attack
                    if attack_row in range(n) and attack_col in range(n):
                        if matrix[attack_row][attack_col] == KNIGHT:
                            attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    max_knight_attacks_pos = [row, col]

    if max_knight_attacks_pos:
        matrix[max_knight_attacks_pos[0]][max_knight_attacks_pos[1]] = EMPTY
        knights_removed += 1

    else:
        break

print(knights_removed)
