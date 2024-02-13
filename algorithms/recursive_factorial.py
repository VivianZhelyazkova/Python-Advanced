def find_factorial(num):
    if num == 1:
        return num
    return num * find_factorial(num - 1)


number = int(input())

print(find_factorial(number))
