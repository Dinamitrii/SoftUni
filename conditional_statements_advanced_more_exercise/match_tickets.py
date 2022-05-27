budget = float(input())
tickets_category = input()  # "VIP", "Normal"
people_count = int(input())

tickets_price_vip = 499.99
tickets_price_normal = 249.99

transport_price = 0

if 1 <= people_count <= 4:
    transport_price = budget * 0.75
    if tickets_category == "VIP":
        final = tickets_price_vip * people_count
    elif tickets_category == "Normal":
        final = tickets_price_normal * people_count
elif 5 <= people_count <= 9:
    transport_price = budget * 0.60
    if tickets_category == "VIP":
        final = tickets_price_vip * people_count
    elif tickets_category == "Normal":
        final = tickets_price_normal * people_count
elif 10 <= people_count <= 24:
    transport_price = budget * 0.50
    if tickets_category == "VIP":
        final = tickets_price_vip * people_count
    elif tickets_category == "Normal":
        final = tickets_price_normal * people_count
elif 25 <= people_count <= 49:
    transport_price = budget * 0.40
    if tickets_category == "VIP":
        final = tickets_price_vip * people_count
    elif tickets_category == "Normal":
        final = tickets_price_normal * people_count
elif people_count >= 50:
    transport_price = budget * 0.25
    if tickets_category == "VIP":
        final = tickets_price_vip * people_count
    elif tickets_category == "Normal":
        final = tickets_price_normal * people_count

cost = final + transport_price
total = abs(budget - cost)

# print(f"{total:.2f}")
if budget >= cost:
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total:.2f} leva.")
