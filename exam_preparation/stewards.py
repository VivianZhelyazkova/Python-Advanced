from collections import deque

seats = deque(input().split(", "))
first = deque([int(x) for x in input().split(", ")])
second = deque([int(x) for x in input().split(", ")])
rotations = 0
matches = []

while True:
    if rotations == 10:
        break
    if len(matches) == 3:
        break
    first_num = first.popleft()
    second_num = second.pop()
    letter = chr(first_num + second_num)
    first_combination = str(first_num) + letter
    second_combination = str(second_num) + letter

    if first_combination in seats:
        matches.append(first_combination)
        seats.remove(first_combination)
    elif second_combination in seats:
        matches.append(second_combination)
        seats.remove(second_combination)
    else:
        first.append(first_num)
        second.appendleft(second_num)
    rotations += 1

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")
