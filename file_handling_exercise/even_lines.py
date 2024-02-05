import os

path = os.path.join("resources", "text.txt")

symbols = {"-", ",", ".", "!", "?"}
REPLACE = "@"

try:
    with open(path) as f:
        content = [line for index, line in enumerate(f.readlines()) if index % 2 == 0]
except FileNotFoundError:
    print(f"File '{path}' not found!")

for index, line in enumerate(content):
    current_line = line
    for symbol in symbols:
        current_line = current_line.replace(symbol, REPLACE)
    current_line = " ".join(reversed(current_line.split()))
    content[index] = current_line

print(*content, sep="\n")
