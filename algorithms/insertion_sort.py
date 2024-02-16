numbers = [int(x) for x in input().split()]


for index in range(1, len(numbers)):
    left_number_index = index - 1
    current_number = numbers[index]
    while left_number_index >= 0 and numbers[left_number_index] > current_number:
        numbers[left_number_index + 1] = numbers[left_number_index]
        left_number_index -= 1
    numbers[left_number_index + 1] = current_number

print(*numbers)


