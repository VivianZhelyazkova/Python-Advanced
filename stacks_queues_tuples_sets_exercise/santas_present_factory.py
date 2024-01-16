from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_presents = []
is_empty = False

while materials and magic:

    current_box = materials[-1]
    current_magic = magic[0]

    if current_box == 0:
        materials.pop()
        while current_box == 0:
            if not materials:
                is_empty = True
                break
            current_box = materials.pop()
    if current_magic == 0:
        magic.pop()
        while current_magic == 0:
            if not magic:
                is_empty = True
                break
            current_magic = magic.popleft()
    
    if is_empty:
        break

    magic_level = current_box * current_magic

    if magic_level in presents:
        materials.popleft()
        magic.pop()
        present = presents[magic_level]
        crafted_presents.append(present)

    elif magic_level < 0:
        materials.popleft()
        magic.pop()
        new_value = current_box + current_magic
        materials.append(new_value)

    elif magic_level not in presents and magic_level > 0:
        magic.pop()
        current_box += 15


