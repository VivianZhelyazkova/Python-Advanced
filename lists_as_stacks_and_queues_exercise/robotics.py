robots = input().split(";")
robots_deque = {}

for robot in robots:
    name, time = robot.split("-")
    robots_deque[name] = int(time)

hours, minutes, seconds = input().split(":")

product = input()
while product != "End":
    

    product = input()