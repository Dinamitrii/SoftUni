chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()  # [Spring, Summer, Аutumn, Winter]
holiday = input()  # [Y – да / N - не]

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

chrysanthemums_total = chrysanthemums_count * chrysanthemums_price
roses_total = roses_count * roses_price
tulips_total = tulips_count * tulips_price
