from itertools import chain

rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

# flattened_matrix = []
#
# for row in matrix:
#     for num in row:
#         flattened_matrix.append(num)
#
# print(flattened_matrix)


flatten = list(chain.from_iterable(matrix))