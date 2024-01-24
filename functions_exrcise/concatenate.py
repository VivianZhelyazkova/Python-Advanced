def concatenate(*args, **kwargs):
    string = ""
    for el in args:
        string += el
    for key, value in kwargs.items():
        if key in string:
            string = string.replace(key,value)
    return string

