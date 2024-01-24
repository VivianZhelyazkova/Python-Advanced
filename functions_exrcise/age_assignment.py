def age_assignment(*args, **kwargs):
    result = ""
    sorted_names = sorted(args)
    for name in sorted_names:
        result += f"{name} is {kwargs[name[0]]} years old.\n"
    return result
