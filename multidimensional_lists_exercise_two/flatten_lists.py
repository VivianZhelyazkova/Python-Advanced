from functools import reduce

matrix = [[int(x) for x in part.split()] for part in input().split("|")]

[print(*row, end=' ') for row in reversed(matrix) if row]
