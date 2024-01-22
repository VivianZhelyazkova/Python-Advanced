matrix = [[x for x in part if x.isnumeric()] for part in input().split("|")]

[print(*row) for row in matrix]