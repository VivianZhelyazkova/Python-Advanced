from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes < 5 and chocolates and milk:
    last_chocolate = chocolates[-1]
    first_milk = milk[0]
    is_invalid = False
    while last_chocolate <= 0:
        chocolates.pop()
        if not chocolates:
            is_invalid = True
            break
        last_chocolate = chocolates[-1]
    while first_milk <= 0:
        milk.popleft()
        if not milk:
            is_invalid = True
            break
        first_milk = milk[0]
    if is_invalid:
        break

    if last_chocolate == first_milk:
        milkshakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if len(chocolates) > 0:
    chocolates_str = [str(x) for x in chocolates]
    print(f"Chocolate:", ", ".join(chocolates_str))
else:
    print("Chocolate: empty")
if len(milk) > 0:
    milk_str = [str(x) for x in milk]
    print("Milk:", ", ".join(milk_str))
else:
    print("Milk: empty")