number = int(input())

cars_in = set()

for _ in range(number):
    command, plate = input().split(", ")
    cars_in.add(plate)