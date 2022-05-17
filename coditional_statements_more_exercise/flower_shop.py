from math import ceil, floor

magnolias_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

magnolias_price = 3.25
hyacinth_price = 4
roses_price = 3.50
cactus_price = 8

total_sum = magnolias_count * magnolias_price + hyacinth_count * hyacinth_price + roses_count * roses_price + cactus_count * cactus_price

tax = total_sum * 0.05

profit = total_sum - tax

total = abs(profit - present_price)

if profit >= present_price:
    print(f"She is left with {floor(total)} leva.")
else:
    print(f"She will have to borrow {ceil(total)} leva.")
