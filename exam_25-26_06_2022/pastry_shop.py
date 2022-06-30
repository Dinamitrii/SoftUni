sweets = input()
sweets_count = int(input())
day_of_december = int(input())

price_per_one = 0

if day_of_december <= 15:
    if sweets == "Cake":
        price_per_one = 24
    elif sweets == "Souffle":
        price_per_one = 6.66
    elif sweets == "Baklava":
        price_per_one = 12.60
elif day_of_december > 15:
    if sweets == "Cake":
        price_per_one = 28.70
    elif sweets == "Souffle":
        price_per_one = 9.80
    elif sweets == "Baklava":
        price_per_one = 16.98

final_price = sweets_count * price_per_one

if day_of_december <= 22:
    if 100 <= final_price <= 200:
        final_price = final_price * 0.85
    elif final_price > 200:
        final_price = final_price * 0.75

if day_of_december <= 15:
    final_price = final_price * 0.90

print(f"{final_price:.2f}")
