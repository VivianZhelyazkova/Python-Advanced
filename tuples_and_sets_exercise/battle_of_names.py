number = int(input())
set_odd = set()
set_even = set()

for num in range(number):
    name = input()
    row = num + 1
    name_sum = int(sum(map(ord, name)) / row)
    if name_sum % 2 == 0:
        set_even.add(name_sum)
    else:
        set_odd.add(name_sum)

if sum(set_even) == sum(set_odd):
    print(*set_even.union(set_odd), sep=", ")
elif sum(set_even) < sum(set_odd):
    print(*set_odd.difference(set_even), sep=", ")
else:
    print(*set_odd.symmetric_difference(set_even),sep=", ")

