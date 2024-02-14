numbers = [int(x) for x in input().split()]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(*numbers)
