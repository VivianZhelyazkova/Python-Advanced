sequence = input()
parentheses = []
symbols = {")": "(", "}": "{", "]": "["}
for char in sequence:
    if char == "(":
        parentheses.append(char)
    elif char == ")":
        parentheses.pop()
