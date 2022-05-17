from math import floor, ceil

square_meters_vineyard = int(input())
grape_per_square_meter = float(input())
liters_wine_needed = int(input())
workers_count = int(input())

percent_for_making_wine = 40

harvest = square_meters_vineyard * grape_per_square_meter

wine = (harvest * percent_for_making_wine) / 100 / 2.5

wine_left = abs(wine - liters_wine_needed)

wine_for_worker = wine_left / workers_count

if wine >= liters_wine_needed:
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(wine_left)} liters left -> {ceil(wine_for_worker)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(wine_left)} liters wine needed.')
