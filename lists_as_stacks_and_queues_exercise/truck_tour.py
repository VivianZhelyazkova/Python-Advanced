from collections import deque

pumps = int(input())
petrol_pumps = deque()

for i in range(pumps):
    petrol_pumps.append(input().split())
