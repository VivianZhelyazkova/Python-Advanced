from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(';'):
    name,time = r.split("-")
    robots[name] = [int(time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

product = input()
products = deque()

while product != "End":
    products.append(product)
    product = input()

