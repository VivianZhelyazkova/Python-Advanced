import re

rows, cols = [int(x) for x in input().split()]

matrix = [int(x) for x in input().split() for row in range(rows)]

command = input()
regex = r"/^swap( \d+){4}/gm"

while command != "END":
    match = re.search(command, regex)
    print(match)
    if match:
        print(command)
    else:
        print("Invalid input!")
    command = input()