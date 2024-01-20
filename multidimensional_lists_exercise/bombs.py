n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

indices = input().split()

indices_matrix = []


def are_coordinates_valid(x, y, lenght):
    if x < 0 or y < 0:
        return False
    if x > lenght or y > lenght:
        return False
    return True


def generate_bomb_hit_box(row, col):
    hit_box = [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1],
               [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]]
    return hit_box


def validate_coordinates(some_list):
    valid_coords = []
    for coord in some_list:
        if are_coordinates_valid(coord[0], coord[1], n):
            valid_coords.append(coord)
    return valid_coords


for el in indices:
    indices_matrix.append([int(n) for n in el.split(",")])

for coordinate in indices_matrix:
    row, col = coordinate
    bomb = matrix[row][col]
    if bomb <= 0:
        continue
    bomb_hit_box = generate_bomb_hit_box(row, col)
    bomb_hit_box = validate_coordinates(bomb_hit_box)
    for c in bomb_hit_box:
        x, y = c
        if matrix[x][y] > 0:
            matrix[x][y] -= bomb
        matrix[row][col] = 0
