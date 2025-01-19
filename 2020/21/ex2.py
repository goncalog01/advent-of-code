with open("input.txt", "r") as f:
    foods = f.read().splitlines()

allergens = {}

for food in foods:
    food_ingredients = food.split(" (")[0].split()
    food_allergens = food.split(" (")[1][:-1].split("contains ")[1].split(", ")
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

sorted_allergens = []

for allergen in allergens:
    sorted_allergens += [allergen]

sorted_allergens.sort()

canonical_dangerous_ingredient_list = ""

for allergen in sorted_allergens:
    canonical_dangerous_ingredient_list += allergens[allergen][0] + ","

print(canonical_dangerous_ingredient_list[:-1])