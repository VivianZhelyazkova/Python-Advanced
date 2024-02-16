from collections import deque

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])
PRESENTS = {
    range(100 - 200): "Gemstone",
    range(200 - 300): "Porcelain Sculpture",
    range(300 - 400): "Gold",
    range(400 - 500): "Diamond Jewellery"
}

while materials and magic_level:
