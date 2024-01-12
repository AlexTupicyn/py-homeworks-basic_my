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

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish)
        for ingredient in ingredients:
            ingredient_name = ingredient.get('ingredient_name')
            if ingredient_name not in ingredients_list.keys():
                ingredients_list.setdefault(ingredient_name, {
                    'measure': ingredient.get('measure'),
                    'quantity': int(ingredient.get('quantity')) * person_count
                })
            else:
                quantity = int(ingredients_list.get(ingredient_name).get('quantity')) + \
                           int(ingredient.get('quantity')) * person_count
                ingredients_list[ingredient_name] = {
                    'measure': ingredient.get('measure'),
                    'quantity': quantity}
    return ingredients_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))