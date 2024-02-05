import os

path = os.path.join("resources", "text.txt")

symbols = {"-", ",", ".", "!", "?"}
REPLACE = "@"

with open(path) as f:
    content = [line for index, line in enumerate(f.readlines()) if index % 2 == 0]

for line in content:
    for symbol in symbols:
        