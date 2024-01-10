sequence = input()
parentheses = []
symbols = {")": "(", "}": "{", "]": "["}
is_balanced = True
for char in sequence:
    if char not in symbols:
        parentheses.append(char)
    else:
        popped = parentheses.pop() if parentheses else ""
        if popped != symbols[char]:
            is_balanced = False

if is_balanced and not parentheses:
    print("YES")
else:
    print("NO")

