number = int(input())
table = set()

for _ in range(number):
    for element in input().split():
        table.add(element)

print(*table, sep="\n")
