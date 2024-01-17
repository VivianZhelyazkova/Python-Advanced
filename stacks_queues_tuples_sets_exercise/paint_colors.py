from collections import deque

string = deque(input().split())

colors = ("red", "yellow", "blue", "orange", "purple", "green")
secondary_colors = {
    "green": {"blue", "yellow"},
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"}
}

colors_made = []

while string:

    first = string.popleft()
    last = string.pop() if string else ""

    for color in (first + last, last + first):
        if color in colors:
            colors_made.append(color)

    else:
        for char in (first[:-1], last[:-1]):
            if char:
                string.insert(len(string) // 2, char)

for color in set(secondary_colors.keys()).intersection(colors_made):
    if not secondary_colors[color].issubset(colors_made):
        colors_made.remove(color)
print(colors_made)
