from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())


def making_honey(bee, nect, symb):
    result = 0
    if symb == '+':
        result = bee + nect
    elif symb == '-':
        result = bee - nect
    elif symb == '*':
        result = bee * nect
    elif symb == '/':
        if nect == 0:
            result = 0
        else:
            result = bee / nect
    return abs(result)


total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    symbol = symbols.popleft()
    honey = 0
    if current_nectar < current_bee:
        while current_nectar < current_bee:
            bees.appendleft(current_bee)
    honey = making_honey(current_bee, current_nectar, symbol)
    total_honey += honey

print(f"Total honey made: {total_honey}")

if bees:
    print("Bees left: ", end="")
    print(*bees, sep=", ")
if nectar:
    print("Nectar left: ", end="")
    print(*nectar, sep=", ")