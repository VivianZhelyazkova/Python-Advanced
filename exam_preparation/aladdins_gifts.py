from math import ceil
from collections import deque

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])

PRESENTS = {
    range(100, 200): "Gemstone",
    range(200, 300): "Porcelain Sculpture",
    range(300, 400): "Gold",
    range(400, 500): "Diamond Jewellery"
}
presents_made = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            result = current_material * 2 + current_magic * 3
        else:
            result *= 2
    if result > 499:
        result = ceil(result/2)
    for k, v in PRESENTS.items():
        if result in k:
            presents_made[v] += 1
            break
pair_made = False
if presents_made["Gemstone"] > 0 and presents_made["Porcelain Sculpture"] > 0:
    pair_made = True
if presents_made["Gold"] > 0 and presents_made["Diamond Jewellery"] > 0:
    pair_made = True

if pair_made:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
sorted_presents = dict(sorted(presents_made.items(), key=lambda x: x[0]))
for gift, count in sorted_presents.items():
    if count:
        print(f"{gift}: {count}")
