from collections import deque

monsters = deque([int(x) for x in input().split(",")])
strikes = deque([int(x) for x in input().split(",")])

monsters_killed = 0

while monsters and strikes:

    current_monster = monsters.popleft()
    current_strike = strikes.pop()

    if current_strike >= current_monster:
        impact_left = current_strike - current_monster
        monsters_killed += 1
        if impact_left > 0:
            if strikes:
                strikes[-1] += impact_left
            else:
                strikes.append(impact_left)
    else:
        current_monster -= current_strike
        monsters.append(current_monster)


if not monsters:
    print("All monsters have been killed!")
if not strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")