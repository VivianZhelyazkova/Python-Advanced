from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    if current_bottle > current_cup:
        wasted_water += current_bottle - current_cup
    current_cup -= current_bottle
    if current_cup <= 0:
        continue
    else:
        cups.appendleft(current_cup)

if not cups:
    print(f"Bottles:", *bottles)

if not bottles:
    print(f"Cups:", *cups)

print(f"Wasted litters of water: {wasted_water}")
