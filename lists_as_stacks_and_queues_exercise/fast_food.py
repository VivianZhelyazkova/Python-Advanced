from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

for index in range(len(orders)):

    if food >= orders[0]:
        food -= orders[0]
        orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print("Orders left: ", end="")
    print(*orders, sep=" ")
