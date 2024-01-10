from collections import deque

water = int(input())

name = input()
queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()

while command != 'End':
    if "refill" in command:
        liters = int(command.split()[1])
        water += liters
    else:
        name = queue.popleft()
        if water >= int(command):
            water -= int(command)
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input()

print(f"{water} liters left")