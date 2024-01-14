number = int(input())
guests = set()

for _ in range(number):
    guests.add(input())

vip = set()
regular = set()

for guest in guests:
    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

guest = input()

while guest != "END":

    if len(guest) == 8:
        if guest in vip:
            vip.remove(guest)
        elif guest in regular:
            regular.remove(guest)
    guest = input()

sorted_vip = sorted(vip)
sorted_regular = sorted(regular)


print(len(vip) + len(regular))

if len(sorted_vip) > 0:
    print(*sorted_vip, sep="\n")
if len(sorted_regular) > 0:
    print(*sorted_regular, sep="\n")
