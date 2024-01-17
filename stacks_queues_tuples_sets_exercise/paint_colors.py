from math import ceil
from collections import deque

string = deque(input().split())

main_colors = ("red", "yellow", "blue")
secondary_colors = ("orange", "purple", "green")

colors_made = []


def removesuffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    else:
        return text


while string:
    if len(string) > 1:
        first = string.popleft()
        last = string.pop()
        color_1 = first + last
        color_2 = last + first

        if color_1 in main_colors:
            colors_made.append(color_1)
        if color_2 in main_colors:
            colors_made.append(color_2)

        if color_1 in secondary_colors:
            colors_made.append(color_1)
        if color_2 in secondary_colors:
            colors_made.append(color_2)

        if (color_1 not in main_colors
                and color_2 not in main_colors
                and color_1 not in secondary_colors
                and color_2 not in secondary_colors):
            first = removesuffix(first, first[-1])
            last = removesuffix(last, last[-1])
            index = ceil(len(string) / 2)
            if first:
                string.insert(index, first)
                index += 1
            if last:
                string.insert(index, last)
    else:
        color = string.pop()
        if color in main_colors:
            colors_made.append(color)

        elif color in secondary_colors:
            colors_made.append(color)

if "orange" in colors_made:
    if "red" not in colors_made or "yellow" not in colors_made:
        colors_made.remove("orange")
if "purple" in colors_made:
    if "red" not in colors_made or "blue" not in colors_made:
        colors_made.remove("purple")
if "green" in colors_made:
    if "blue" not in colors_made or "yellow" not in colors_made:
        colors_made.remove("green")

print(colors_made)
