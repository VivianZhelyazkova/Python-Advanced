import os

text_path = os.path.join("resources", "text.txt")
output_path = os.path.join("resources", "output.txt")

try:
    with open(text_path) as f:
        lines = f.readlines()

except FileNotFoundError:
    print(f"Fine {text_path} not found!")

with open(output_path, "w") as f:
    for index, line in enumerate(lines):
        letters, punct_marks = 0, 0

        for char in line:
            if char.isalpha():
                letters += 1
            elif not char.isalnum() and not char.isspace():
                punct_marks += 1
        new_line = f"Line {index + 1}: {line} ({letters})({punct_marks})\n"
        f.write(new_line)
