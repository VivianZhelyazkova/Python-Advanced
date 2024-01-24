def func_executor(*some_funcs):
    total_result = ""
    for el in some_funcs:
        func, args = el
        result = func(*args)
        total_result += f"{func.__name__} - {result}\n"
    return total_result


