def shopping_cart(*args):
    result = ""
    cart = {
        "Soup": set(),
        "Pizza": set(),
        "Dessert": set()
    }
    for item in args:
        if item == "Stop":
            break
        else:
            meal, product = item
            if meal == "Soup":
                if len(cart[meal]) < 3:
                    cart[meal].add(product)
            elif meal == "Pizza":
                if len(cart[meal]) < 4:
                    cart[meal].add(product)
            elif meal == "Dessert":
                if len(cart[meal]) < 2:
                    cart[meal].add(product)

    sorted_cart = dict(sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])))
    if not any(sorted_cart.values()):
        return "No products in the cart!"

    for meal, products in sorted_cart.items():
        result += f"{meal}:\n"
        for product in sorted(list(products)):
            result += f" - {product}\n"
    return result

