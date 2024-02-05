import os

text_path = os.path.join("resources", "text.txt")
output_path = os.path.join("resources", "output.txt")

try:
    with open(text_path) as f:
        lines = f.readlines()

except FileNotFoundError:
    print(f"Fine {text_path} not found!")

for index, line in enumerate(lines):
    letters = 0
    punct_marks = 0

    new_line = f"Line {index + 1}: {line}