from collections import deque

number_of_pumps = int(input())
pumps = deque()
# pumps = deque([[22, 5, 0], [14, 10, 1], [52, 7, 2], [21, 12, 3], [36, 9, 4]])
for index in range(number_of_pumps):
    pump_info = [int(x) for x in input().split()]
    pump_info.append(index)
    pumps.append(pump_info)

current_petrol = 0
counter = 0

while counter < len(pumps):
    petrol, distance, _ = pumps[counter]
    current_petrol += petrol

    if distance > current_petrol:
        pumps.rotate(-1)
        counter = 0
        current_petrol = 0
        continue

    current_petrol -= distance

    counter += 1
starting_pump = pumps.popleft()
petrol, distance, pump_index = starting_pump
print(pump_index)