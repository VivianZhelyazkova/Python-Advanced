from collections import deque

monsters_armor = deque([int(x) for x in input().split()])
striking_impact = deque([int(x) for x in input().split()])


while monsters_armor and striking_impact:

    current_monster = monsters_armor.pop()
    current_strike = striking_impact.popleft()

    if current_strike >= current_monster:

        