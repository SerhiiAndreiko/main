def format_ingredients(items):
    recipe = ""
    for i in range(len(items)):
        if i == len(items) - 1:
            recipe += " and " + items[i]
        else:
            recipe += items[i] + " "
    return recipe

items = ['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']
print(format_ingredients(items)), (items)

