def even_odd(*args):
    cmd = args[-1]
    if cmd == 'even':
        return [x for x in args[:-1] if int(x) % 2 == 0]
    else:
        return [x for x in args[:-1] if int(x) % 2 != 0]


