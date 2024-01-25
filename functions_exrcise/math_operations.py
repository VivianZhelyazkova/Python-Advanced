from collections import deque


def math_operations(*args, **kwargs):
    index = 0
    for num in args:
        if index == len(kwargs):
            index = 0
        key = list(kwargs.keys())[index]
        if key == "a":
            kwargs[key] += num
        elif key == "s":
            kwargs[key] -= num
        elif key == "d":
            if num != 0:
                kwargs[key] /= num
        elif key == "m":
            kwargs[key] *= num
        index += 1
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    result = ""
    for key, val in sorted_dict.items():
        result += f"{key}: {val:.1f}\n"
    return result

