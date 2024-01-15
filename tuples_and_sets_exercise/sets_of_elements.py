symbol_1, symbol_2 = input().split()
num_1 = int(symbol_1)
num_2 = int(symbol_2)
set_1 = set()
set_2 = set()

for _ in range(num_1):
    set_1.add(int(input()))

for _ in range(num_2):
    set_2.add(int(input()))

print(*set_1.intersection(set_2), sep="\n")
# print(*(set_1 & set_2), sep="\n")
