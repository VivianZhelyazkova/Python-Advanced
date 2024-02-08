from collections import deque

worms = deque([int(x) for x in input().split()])
holes = deque([int(x) for x in input().split()])

starting_worms = len(worms)
matches = 0

while holes and worms:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm != current_hole:

        current_worm -= 3

        if current_worm > 0:
            worms.append(current_worm)
    else:
        matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if matches == starting_worms:
    print("Every worm found a suitable hole!")
else:
    if worms:
        print(f"Worms left: {', '.join([str(x) for x in worms])}")
    else:
        print("Worms left: none")

if holes:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
else:
    print("Holes left: none")
