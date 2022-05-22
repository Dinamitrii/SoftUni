budget = int(input())
season = input()
count_people = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if count_people <= 6:
    price = price * 0.90
elif 7 <= count_people <= 11:
    price = price * 0.85
else:
    price = price * 0.75

if count_people % 2 == 0:
    if season != "Autumn":
        price = price * 0.95

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
