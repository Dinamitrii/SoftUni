mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = int(input())

bonito_price = mackerel_price + (mackerel_price * 0.60)
bonito_total = bonito_kg * bonito_price

scad_price = sprat_price + (sprat_price * 0.80)
scad_total = scad_kg * scad_price

mussels_price = 7.50
mussels_total = mussels_kg * mussels_price

total_bill = bonito_total + scad_total + mussels_total

print(f'{total_bill:.2f}')
