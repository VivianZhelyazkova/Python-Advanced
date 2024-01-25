def even_odd_filter(**kwargs):

    if 'odd' in kwargs:
        kwargs['odd'] = [x for x in kwargs.values() if x % 2 != 0]
    if 'even' in kwargs:
        kwargs['even'] = [x for x in kwargs.values() if x % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True))

