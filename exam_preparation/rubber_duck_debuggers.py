from collections import deque

time = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

rubber_ducks = {
    range(0, 61): "Darth Vader Ducky",
    range(61, 121): "Thor Ducky",
    range(121, 181): "Big Blue Rubber Ducky",
    range(181, 241): "Small Yellow Rubber Ducky"
}
HIGHEST_RANGE = 240
ducks_given = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0

}

while time and tasks:

    current_time = time.popleft()
    current_task = tasks.pop()

    result = current_task * current_time

    if result > HIGHEST_RANGE:
        current_task -= 2
        tasks.append(current_task)
        time.append(current_time)
        continue

    for k, v in rubber_ducks.items():
        if result in k:
            duck = v
            ducks_given[duck] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, count in ducks_given.items():
    print(f"{duck}: {count}")
