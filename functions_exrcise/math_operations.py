def operations(operator, number, some_dict):
    if operator == "a":
        some_dict[operator] += number
    elif operator == "s":
        some_dict[operator] -= number
    elif operator == "d":
        if number != 0:
            some_dict[operator] /= number
    elif operator == "m":
        some_dict[operator] *= number


def math_operations(*args, **kwargs):
    index = 0
    for num in args:
        if index == len(kwargs):
            index = 0
        key = list(kwargs.keys())[index]
        operations(key, num, kwargs)
        index += 1
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))

    return "\n".join(f"{key}: {val:.1f}" for key, val in sorted_dict)
