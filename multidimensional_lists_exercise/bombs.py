n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

indices = input().split()

indices_matrix = []


def are_coordinates_valid(x, y, some_matrix):
    if x < 0 or y < 0:
        return False
    if x > len(some_matrix[0]) or y > len(some_matrix[0]):
        return False
    return True


def generate_bomb_hit_box(row, col):
    hit_box = [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1],
               [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]]
    return hit_box


for el in indices:
    indices_matrix.append([int(n) for n in el.split(",")])

for coordinate in indices_matrix:
    row, col = coordinate
    bomb = matrix[row][col]
    bomb_hit_box = generate_bomb_hit_box(row, col)
