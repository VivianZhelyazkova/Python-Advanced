def sum_numbers(list_of_numbers, index):
    if index == len(list_of_numbers) - 1:
        return list_of_numbers[index]
    return list_of_numbers[index] + sum_numbers(list_of_numbers, index + 1)


numbers = [int(x) for x in input().split()]
print(sum_numbers(numbers, 0))
