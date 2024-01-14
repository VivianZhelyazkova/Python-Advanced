numbers = tuple(float(x) for x in input().split())

set_numbers = set(numbers)

for number in numbers:
    if number in set_numbers:
        print(f"{number:.1f} - {numbers.count(number)} times")
        set_numbers.remove(number)
