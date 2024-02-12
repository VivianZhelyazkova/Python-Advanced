from collections import deque

caffeine_grams = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])

MAX_CAFFEINE = 300
caffeine_consumed = 0

while caffeine_grams and energy_drinks:
    current_caffeine = caffeine_grams.pop()
    current_drink = energy_drinks.popleft()
    result = current_caffeine * current_drink

    if result + caffeine_consumed <= MAX_CAFFEINE:
        caffeine_consumed += result
    else:
        energy_drinks.append(current_drink)
        caffeine_consumed -= 30
        if caffeine_consumed < 0:
            caffeine_consumed = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_consumed} mg caffeine.")
