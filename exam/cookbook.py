def cookbook(*args):
    result = ""
    cook_book = {}
    for name, cuisine, ingredients in args:
        if cuisine not in cook_book:
            cook_book[cuisine] = {name: ingredients}
        else:
            cook_book[cuisine][name] = ingredients

    sorted_cookbook = dict(sorted(cook_book.items(), key=lambda x: (-len(x[1]), x[0])))
    for cuisine, recipes in sorted_cookbook.items():
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"

        for recipe, ingredients in sorted(recipes.items()):
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"
    return result

