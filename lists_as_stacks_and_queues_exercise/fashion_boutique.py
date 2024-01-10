clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack_capacity = rack_capacity
racks = 0

while clothes:

    if current_rack_capacity >= clothes[-1]:
        current_rack_capacity -= clothes.pop()

    else:
        racks += 1
        current_rack_capacity = rack_capacity

if current_rack_capacity < rack_capacity:
    racks += 1

print(racks)
