import math

expression = input().split()

expression_copy = expression.copy()
last_operator_index = 0

current_sum = None

for index, char in enumerate(expression):

    if not char.isnumeric():
        if last_operator_index == 0:
            start = last_operator_index
        else:
            start = last_operator_index + 1
        last_operator_index = index
        end = index
        numbers_as_str = expression[start:end]
        numbers = list(int(x) for x in numbers_as_str)

        if current_sum is not None:
            numbers.insert(0, current_sum)

        if char == "*":
            current_sum = math.prod(numbers)
        elif char == "+":
            current_sum = sum(numbers)
        elif char == "-":
            total = numbers[0]
            for i in range(1, len(numbers)):
                total -= numbers[i]
            current_sum = total
        elif char == "/":
            total = numbers[0]
            for i in range(1, len(numbers)):
                total /= numbers[i]
            current_sum = int(total)

print(current_sum)
