from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

while materials and magic:

    current_box = materials[-1]
    current_magic = magic[0]

    magic_level = current_box * current_magic

    if