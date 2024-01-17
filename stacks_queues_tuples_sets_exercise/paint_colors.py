from collections import deque

string = deque(input().split())

main_colors = ("red", "yellow", "blue")
secondary_colors = ("orange", "purple", "green")

colors_made = []

while string:
    if len(string) > 1:
        first = string.popleft()
        last = string.pop()
        color = first + last

        if color in main_colors:
            colors_made.append(color)

        elif color in secondary_colors:
            colors_made.append(color)

        else:
            first = list(first)
            first.pop()
            last = list(last)
            last.pop()

            first = "".join(first)
            last = "".join(last)
            index = len(string) // 2
            string.insert(index, first)
            string.insert(index + 1, last)
    else:
        color = string
        if color in main_colors:
            colors_made.append(color)

        elif color in secondary_colors:
            colors_made.append(color)


if "orange" in colors_made:
    if "red" not in colors_made and "yellow" not in colors_made:
        colors_made.remove("orange")
if "purple" in colors_made:
    if "red" not in colors_made and "blue" not in colors_made:
        colors_made.remove("purple")
if "green" in colors_made:
    if "blue" not in colors_made and "yellow" not in colors_made:
        colors_made.remove("green")

print(colors_made)
