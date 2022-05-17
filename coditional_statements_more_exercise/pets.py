from math import ceil, floor

days_vacation = int(input())
food_dropped_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())

dog_food_total = days_vacation * dog_food_per_day_kg
cat_food_total = days_vacation * cat_food_per_day_kg
turtle_food_total_kg = (days_vacation * turtle_food_per_day_g) / 1000

food_total_kg = dog_food_total + cat_food_total + turtle_food_total_kg

food_final = abs(food_dropped_kg - food_total_kg)

if food_total_kg <= food_dropped_kg:
    print(f'{floor(food_final)} kilos of food left.')
else:
    print(f'{ceil(food_final)} more kilos of food are needed.')
