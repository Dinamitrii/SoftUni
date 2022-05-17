x = float(input())
y = float(input())
h = float(input())

side_walls = (x * y) * 2 - (1.5 * 1.5) * 2
front_rear_walls = (x * x) * 2 - (1.2 * 2)
total_area_walls = side_walls + front_rear_walls

roof_main = (x * y) * 2
roof_side = (x * h / 2) * 2
total_roof = roof_main + roof_side

green_paint = total_area_walls / 3.4
red_paint = total_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
