numbers = [int(x) for x in input().split()]
target = int(input())

while numbers:
    mid_num = numbers[len(numbers) // 2]
    index = numbers.index(mid_num)
    if mid_num == target:
        print(index)
        break
    elif mid_num > target:
        numbers = numbers[:index]
    elif mid_num < target:
        numbers = numbers[index + 1:]
