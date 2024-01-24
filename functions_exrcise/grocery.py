def grocery_store(**kwargs):
    sorted_list = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    receipt = ""
    for name, quantity in sorted_list.items():
        receipt += f"{name}: {quantity}\n"
    return receipt

