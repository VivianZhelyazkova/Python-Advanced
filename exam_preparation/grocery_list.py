def shop_from_grocery_list(budget, grocery_list, *args):
    for item, price in args:
        if item in grocery_list:
            if budget >= price:
                budget -= price
                grocery_list.remove(item)
            else:
                break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
