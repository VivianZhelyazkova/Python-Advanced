numbers = [int(x) for x in input().split()]

for i in range(len(numbers)):
    min_num_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_num_index]:
            min_num_index = j
    numbers[min_num_index], numbers[i] = numbers[i], numbers[min_num_index]

print(*numbers)
