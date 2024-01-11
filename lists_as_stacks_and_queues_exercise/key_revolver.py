from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])

value = int(input())

current_barrel = barrel_size
bullets_shot = 0

while bullets:

    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    current_barrel -= 1
    bullets_shot += 1
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    if current_barrel == 0 and bullets:
        print("Reloading!")
        current_barrel = barrel_size

    if len(locks) == 0:
        money_spend = bullets_shot * bullet_price
        money_earned = value - money_spend
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
