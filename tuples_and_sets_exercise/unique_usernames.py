number = int(input())
sett = set()
for _ in range(number):
    sett.add(input())

print(*sett, sep="\n")