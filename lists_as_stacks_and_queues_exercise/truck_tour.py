from collections import deque

number_of_pumps = int(input())
pumps = deque()

for _ in range(number_of_pumps):
    pumps.append(input().split())

for pump in pumps:
    liters, kilometers = pump
    if liters >= kilometers:
        start = 