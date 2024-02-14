numbers = [int(x) for x in input().split()]
target = int(input())

start = 0
end = len(numbers) - 1
index = -1
while start <= end:
    mid_index = end + start // 2
    if numbers[mid_index] == target:
        index = mid_index
        break
    elif numbers[mid_index] < target:
        start = mid_index + 1
    elif numbers[mid_index] > target:
        end = mid_index - 1

print(index)
