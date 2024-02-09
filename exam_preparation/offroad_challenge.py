from collections import deque

fuel = deque(int(x) for x in input().split())
consumption_indexes = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

altitude_counter = []

for index in range(1, 5):
    current_fuel = fuel.pop()
    current_consumption = consumption_indexes.popleft()
    needed = fuel_needed.popleft()

    if current_fuel - current_consumption >= needed:
        altitude_counter.append(f"Altitude {index}")
        print(f"John has reached: Altitude {index}")
    else:

        print(f"John did not reach: Altitude {index}")
        break

if len(altitude_counter) == 4:
    print(f"John has reached all the altitudes and managed to reach the top!")

elif not altitude_counter:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(altitude_counter)}")
