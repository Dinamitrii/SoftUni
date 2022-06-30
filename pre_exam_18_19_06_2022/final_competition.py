dancers = int(input())
points = float(input())
season = input()
place = input()

expences = 0
sum_profit = 0
charity = 0.75
money_for_charity = 0

if season == "summer":
    if place == "Bulgaria":
        expences = 0.95
        sum_profit = (dancers * points) * expences
    elif place == "Abroad":
        expences = 0.90
        sum_profit = ((dancers * points) * expences) * 1.50
elif season == "winter":
    if place == "Bulgaria":
        expences = 0.92
        sum_profit = (dancers * points) * expences
    elif place == "Abroad":
        expences = 0.85
        sum_profit = ((dancers * points) * expences) * 1.50

money_for_charity = sum_profit * charity
money_per_dancer = (sum_profit - money_for_charity) / dancers

print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
