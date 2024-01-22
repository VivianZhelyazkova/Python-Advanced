rows, cols = [int(x) for x in input().split()]

snake = input()
counter = 0
matrix = []

for row_index in range(rows):
    matrix.append([])
    if row_index % 2 == 0:
        for col_index in range(cols):
            if counter == len(snake):
                counter = 0
            matrix[row_index].append(snake[counter])
            counter += 1
    else:
        for col_index in range(cols - 1, -1, -1):
            if counter == len(snake):
                counter = 0
            matrix[row_index].insert(0, snake[counter])
            counter += 1

[print("".join(row)) for row in matrix]
