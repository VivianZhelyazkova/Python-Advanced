player_1, player_2 = input().split(", ")
n = 6
matrix = []
for row in range(n):
    matrix.append(input().split())


def move_player(current_player, enemy_player, some_matrix, some_boolean):
    global player_1_skips, player_2_skips
    player_position = some_matrix[row][col]
    if player_position == EXIT:
        print(f"{current_player} found the Exit and wins the game!")
        exit()
    elif player_position == TRAP:
        print(f"{current_player} is out of the game! The winner is {enemy_player}.")
        exit()
    elif player_position == WALL:
        print(f"{current_player} hits a wall and needs to rest.")
        if some_boolean:
            player_1_skips = True
        else:
            player_2_skips = True


EXIT = "E"
TRAP = "T"
WALL = "W"
EMPTY = "."

player_1_skips = False
player_2_skips = False

while True:
    row, col = [int(x) for x in input() if x.isdigit()]
    if not player_1_skips:
        move_player(player_1, player_2, matrix, True)
    else:
        player_1_skips = False
    row, col = [int(x) for x in input() if x.isdigit()]
    if not player_2_skips:
        move_player(player_2, player_1, matrix, False)
    else:
        player_2_skips = False
