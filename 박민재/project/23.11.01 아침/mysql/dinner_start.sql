SELECT food_type, name, ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
FROM food
JOIN food_type ON food.food_type_id = food_type.id;