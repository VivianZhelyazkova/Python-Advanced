possible_coins = sorted([int(x) for x in input().split(', ')], reverse=True)
target = int(input())
used_coins = {}

for coin in possible_coins:
    if target == 0:
        break
    coins_count = target // coin
    used_coins[coin] = coins_count
    target %= coin
if target:
    print("Error")
else:
    total_coins = sum(used_coins.values())
    print(f"Number of coins to take: {total_coins}")
    for coin, count in used_coins.items():
        if count:
            print(f"{count} coin(s) with value {coin}")
