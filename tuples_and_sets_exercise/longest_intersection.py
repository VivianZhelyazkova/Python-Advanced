number = int(input())
longest = 0
longest_intersection = set()
for _ in range(number):
    first, second = input().split("-")
    first_start, first_end = first.split(",")
    second_start, second_end = second.split(",")

    first_set = set(range(int(first_start), int(first_end) + 1))
    second_set = set(range(int(second_start), int(second_end) + 1))

    intersection = (first_set.intersection(second_set))
    longest = max(len(intersection), longest)
    

