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
        result = bee / nect
    return abs(result)


total_honey = 0

while bees and nectar:

    current_bee = bees[0]
    current_nectar = nectar[-1]

    if current_nectar >= current_bee:
        symbol = symbols.popleft()
        if current_nectar > 0:
            honey = making_honey(current_bee, current_nectar, symbol)
        bees.popleft()
        nectar.pop()
