expression = input()
parentheses = []

for index in range(len(expression)):
    if expression[index] == "(":
        parentheses.append(index)
    elif expression[index] == ")":
        start = parentheses.pop()
        print(expression[start:index + 1])