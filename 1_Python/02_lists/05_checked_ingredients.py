def check_ingredient_match(recipe, ingredients):
    missing_ingredients = []
    wrong_count = 0
    for i in range(0, len(recipe)):
        if recipe[i] != ingredients[i]:
            missing_ingredients.append(recipe[i])
            wrong_count += 1
    percentage = float((len(recipe) - wrong_count) / len(recipe)) * 100
    return percentage, missing_ingredients
