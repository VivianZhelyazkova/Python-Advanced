from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(';'):
    name, time = r.split("-")
    robots[name] = [int(time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

product = input()
products = deque()

while product != "End":
    products.append(product)
    product = input()

while products:

    factory_time += timedelta(seconds=1)
    product = products.popleft()

    free_robots = []

    for name, info in robots.items():
        if info[1] != 0:
            robots[name][1] -= 1

        if info[1] == 0:
            free_robots.append([name, info])
