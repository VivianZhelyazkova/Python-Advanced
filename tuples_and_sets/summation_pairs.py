numbers = [int(x) for x in input().split()]
target = int(input())

for index, number in enumerate(numbers):
    for i in range(index + 1, len(numbers)):
        if number + numbers[i] == target:
            print(f"{number} + {numbers[i]} = {target}")


