from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_presents = {"Bicycle": 0, "Doll": 0, "Teddy bear": 0, "Wooden train": 0}


while materials and magic:

    current_box = materials.pop()
    current_magic = magic.popleft()

    magic_level = current_box * current_magic

    if magic_level in presents:
        present = presents[magic_level]
        crafted_presents[present] += 1

    elif magic_level < 0:
        new_value = current_box + current_magic
        materials.append(new_value)

    elif magic_level not in presents and magic_level > 0:
        materials.append(current_box + 15)

pair_made = False

if crafted_presents["Doll"] and crafted_presents["Wooden train"]:
    pair_made = True
if crafted_presents["Teddy bear"] and crafted_presents["Bicycle"]:
    pair_made = True

if pair_made:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials = list(reversed(materials))
    print("Materials left: ", end="")
    print(*materials, sep=", ")
if magic:
    print("Magic left: ", end="")
    print(*magic, sep=", ")

for present, count in crafted_presents.items():
    if count:
        print(f"{present}: {count}")
