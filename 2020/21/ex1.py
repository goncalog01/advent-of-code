with open("input.txt", "r") as f:
    foods = f.read().splitlines()

allergens = {}
ingredients = []

for food in foods:
    food_ingredients = food.split(" (")[0].split()
    food_allergens = food.split(" (")[1][:-1].split("contains ")[1].split(", ")
    for ingredient in food_ingredients:
        if ingredient not in ingredients:
            ingredients += [ingredient]
    for allergen in food_allergens:
        if allergen not in allergens.keys():
            allergens[allergen] = food_ingredients.copy()
        else:
            for ingredient in allergens[allergen].copy():
                if ingredient not in food_ingredients:
                    allergens[allergen].remove(ingredient)
        for allerg in allergens:
            if len(allergens[allerg]) == 1:
                for aller in allergens:
                    if aller == allerg:
                        continue
                    elif allergens[allerg][0] in allergens[aller]:
                        allergens[aller].remove(allergens[allerg][0])

without_allergens = []

for ingredient in ingredients.copy():
    no_allergens = True
    for allergen in allergens:
        if ingredient in allergens[allergen]:
            no_allergens = False
            break
    if no_allergens:
        without_allergens += [ingredient]

sum = 0

for food in foods:
    food_ingredients = food.split(" (")[0].split()
    for ingredient in without_allergens:
        if ingredient in food_ingredients:
            sum += 1

print(sum)