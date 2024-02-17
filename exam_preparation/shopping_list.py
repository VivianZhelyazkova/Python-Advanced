def shopping_list(budget, **kwargs):
    bought_products = {}
    result = ""
    if budget < 100:
        return "You do not have enough budget."
    for product, info in kwargs.items():
        cost = info[0] * info[1]
        if len(bought_products) == 5:
            break
        if budget >= cost:
            bought_products[product] = cost
            budget -= cost
    for product, cost in bought_products.items():
        result += f"You bought {product} for {cost:.2f} leva.\n"
    return result
