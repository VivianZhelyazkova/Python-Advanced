from collections import deque

money = deque([int(x) for x in input().split()])
food = deque([int(x) for x in input().split()])
bought_food = 0

while money and food:
    current_money = money.pop()
    current_food = food.popleft()
    if current_money >= current_food:
        bought_food += 1
        change = current_money - current_food
        if len(money) > 0:
            money[-1] += change
        else:
            money.append(change)

if bought_food >= 4:
    print(f"Gluttony of the day! Henry ate {bought_food} foods.")
elif bought_food == 1:
    print("Henry ate: 1 food.")
elif bought_food > 1:
    print(f"Henry ate: {bought_food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")