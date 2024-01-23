def sorting_cheeses(**kwargs):
    result = ""
    sorted_kwargs_by_pieces = dict(sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])))
    for cheese, pieces in sorted_kwargs_by_pieces.items():
        result += cheese + "\n"
        for piece in sorted(pieces,reverse=True):
            result += f'{piece}\n'
    return result


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)