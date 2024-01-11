from collections import deque

number_of_pumps = int(input())
pumps = deque()
current_liters = 0

for index in range(number_of_pumps):
    info = [int(x) for x in input().split()]
    info.append(index)
    pumps.append(info)

counter = 0

while counter < len(pumps):

    liters, kilometers, index = pumps[counter]
    current_liters += liters
    if kilometers > current_liters:
        pumps.rotate(-1)
        current_liters = 0
        counter = 0
        continue
    else:
        current_liters -= kilometers
    counter += 1

starting_pump = pumps.popleft()
fuel, distance, index = starting_pump

print(index)
