from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient_line = file.readline()
            ingredient_name, quantity, measure = ingredient_line.strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredient)
        file.readline()
        cook_book[dish] = ingredients
    print('cool_book = ')
    pprint(cook_book,sort_dicts=False)