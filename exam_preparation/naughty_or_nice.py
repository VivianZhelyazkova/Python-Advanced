def naughty_or_nice_list(some_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    result = ""
    for command in args:
        number = int(command.split("-")[0])
        cmd = command.split("-")[1]
        matching_kids = [kid for kid in some_list if kid[0] == number]
        if len(matching_kids) == 1:
            kid = matching_kids[0]
            some_list.remove(kid)
            if cmd == "Naughty":
                naughty_list.append(kid[1])
            elif cmd == "Nice":
                nice_list.append(kid[1])

    if kwargs:
        for name, cmd in kwargs.items():
            matching_kids = [kid for kid in some_list if kid[1] == name]
            if len(matching_kids) == 1:
                kid = matching_kids[0]
                some_list.remove(kid)
                if cmd == "Naughty":
                    naughty_list.append(kid[1])
                elif cmd == "Nice":
                    nice_list.append(kid[1])

    not_found_list = [kid[1] for kid in some_list]
    if nice_list:
        result += f"Nice: {', '.join(nice_list)}\n"
    if naughty_list:
        result += f"Naughty: {', '.join(naughty_list)}\n"
    if not_found_list:
        result += f"Not found: {', '.join(not_found_list)}"
    return result


