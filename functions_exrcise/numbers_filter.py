def even_odd_filter(**kwargs):
    for cmd, nums in kwargs.items():
        if cmd == 'odd':
            kwargs['odd'] = [x for x in nums if x % 2 != 0]
        elif cmd == 'even':
            kwargs['even'] = [x for x in nums if x % 2 == 0]
    return dict(sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True))

