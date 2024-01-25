nums_input = [int(x) for x in input().split()]


def positive_or_negative(numbers):
    positive = sum([x for x in numbers if x > 0])
    negative = sum([x for x in numbers if x < 0])
    return positive, negative


def print_sums(neg, pos):
    print(f"{neg}\n{pos}")


def find_strongest(pos, neg):
    if abs(neg) > abs(pos):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


positives, negatives = positive_or_negative(nums_input)
print_sums(negatives, positives)
find_strongest(positives, negatives)
