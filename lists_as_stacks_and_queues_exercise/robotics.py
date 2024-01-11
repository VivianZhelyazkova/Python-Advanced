from collections import deque

robots = input().split(";")
robots_deque = deque()

for robot in robots:
    info = robot.split("-")
    robots_deque.append(info)

hours, minutes, seconds = input().split(":")

product = input()
products = deque()
while product != "End":
    products.append(product)
    product = input()

