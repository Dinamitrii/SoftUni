juniors_count = int(input())
seniors_count = int(input())
track_type = input()  # "trail", "cross-country", "downhill" или "road"

juniors_price = 0
seniors_price = 0

if track_type == "trail":
    juniors_price = 5.50
    seniors_price = 7
elif track_type == "cross-country":
    juniors_price = 8
    seniors_price = 9.50
    if (juniors_count + seniors_count) >= 50:
        juniors_price = juniors_price * 0.75
        seniors_price = seniors_price * 0.75
elif track_type == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif track_type == "road":
    juniors_price = 20
    seniors_price = 21.50

total_income = (juniors_count * juniors_price) + (seniors_count * seniors_price)
expenses = total_income * 0.05
final_income = total_income - expenses

print(f"{final_income:.2f}")
