input_file = open("input.txt", "r")
allergen_map = {}
all_ingredients = []
for line in input_file:
    ingredients = list(line.split('(')[0].strip().split())
    allergens = list(line.split('(')[1].replace('(', '').replace(')', '').replace("contains", '').replace(',', '').strip().split())
    all_ingredients.append(ingredients)
    for allergen in allergens:
        if allergen not in allergen_map:
            allergen_map[allergen] = set(ingredients)
        else:
            allergen_map[allergen] = allergen_map[allergen].intersection(set(ingredients))

# for a in allergen_map:
#     print(a, allergen_map[a])
# print()

ing_map = {}
num_allergens = len(allergen_map)

for _ in range(num_allergens):
    for a in allergen_map:
        if len(allergen_map[a]) == 1:
            ing = allergen_map[a].pop()
            ing_map[a] = ing

            for aa in allergen_map:
                allergen_map[aa].discard(ing)

            break

tot = 0
for ings in all_ingredients:
    for ing in ings:
        if ing not in ing_map.values():
            tot += 1

print(tot)

sorted_keys = sorted(ing_map.keys())

str_out = ""
for key in sorted_keys:
    str_out += ing_map[key] + ","

print(str_out[:-1])
