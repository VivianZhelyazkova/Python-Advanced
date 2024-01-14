number = int(input())

cars_in = set()

for _ in range(number):
    command, plate = input().split(", ")
    if command == "IN":
        cars_in.add(plate)
    else:
        cars_in.remove(plate)

if cars_in:
    print(*cars_in, sep='\n')
else:
    print("Parking Lot is Empty")