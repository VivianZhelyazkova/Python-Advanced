import sys

n = 6
trows_count = 3
max_num = sys.maxsize
matrix = []
for row in range(n):
    matrix.append(input().split(" "))

BUCKET = "B"
HIT_BUCKET = "H"
PRIZES = {
    range(100, 200): "Football",
    range(200, 300): "Teddy Bear",
    range(300, max_num): "Lego Construction Set"
}
score = 0

for trow in range(trows_count):
    command = input()
    command = command.replace("(", "").replace(")", "")
    row, col = command.split(", ")
    row = int(row)
    col = int(col)
    if row in range(n) and col in range(n):
        position = matrix[row][col]
        if position == BUCKET:
            for i in range(n):
                if matrix[i][col] != BUCKET:
                    score += int(matrix[i][col])
            matrix[row][col] = HIT_BUCKET
if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
else:
    for k, v in PRIZES.items():
        if score in k:
            print(f"Good job! You scored {score} points, and you've won {v}.")
