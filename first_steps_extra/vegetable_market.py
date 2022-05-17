veg_price = float(input())
fruits_price = float(input())
veg_kg = int(input())
fruits_kg = int(input())

euro = 1.94

veg_total = veg_price * veg_kg
fruits_total = fruits_price * fruits_kg

total = (veg_total + fruits_total) / euro

print(f'{total:.2f}')
