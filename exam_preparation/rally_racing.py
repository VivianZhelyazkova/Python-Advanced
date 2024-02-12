n = int(input())
racing_number = input()
matrix = []
for row in range(n):
    matrix.append(input().split())


def move_car(old_pos, new_pos):
    new_row, new_col = new_pos
    matrix[old_pos[0]][old_pos[1]] = EMPTY
    return [new_row, new_col]


def move_to_tunnel_end(some_matrix, old_pos):
    some_matrix[old_pos[0]][old_pos[1]] = EMPTY
    for row in range(n):
        for col in range(n):
            if some_matrix[row][col] == TUNNEL:
                return [row, col]


DIRECTIONS = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}
TUNNEL = "T"
FINISH = "F"
CAR = "C"
EMPTY = "."
SINGLE_MOVE = 10
TUNNEL_MOVE = 30
passed_kilometers = 0
car_position = [0, 0]

command = input()
while command != "End":
    next_row = car_position[0] + DIRECTIONS[command][0]
    next_col = car_position[1] + DIRECTIONS[command][1]
    next_position = matrix[next_row][next_col]
    car_position = move_car(car_position, [next_row, next_col])
    if next_position == EMPTY:
        passed_kilometers += SINGLE_MOVE
    elif next_position == TUNNEL:
        car_position = move_to_tunnel_end(matrix, car_position)
        passed_kilometers += TUNNEL_MOVE
    elif next_position == FINISH:
        passed_kilometers += SINGLE_MOVE
        matrix[car_position[0]][car_position[1]] = CAR
        print(f"Racing car {racing_number} finished the stage!")
        break
    command = input()

else:
    matrix[car_position[0]][car_position[1]] = CAR
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {passed_kilometers} km.")
[print("".join(row)) for row in matrix]
