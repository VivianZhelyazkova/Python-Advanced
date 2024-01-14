number = int(input())
names = set()
for i in range(number):
    names.add(input())

print(*names, sep="\n")
