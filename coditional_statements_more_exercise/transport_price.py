kilometers = int(input())
day_or_night = input()

taxi_rate_day = 0.79
taxi_rate_night = 0.90
starting_charge = 0.70

taxi_cost_day = starting_charge + (kilometers * taxi_rate_day)
taxi_cost_night = starting_charge + (kilometers * taxi_rate_night)

autobus_price = 0.09

autobus_cost = kilometers * autobus_price

train_price = 0.06

train_cost = kilometers * train_price

if kilometers < 20 and day_or_night == 'day':
    print(f'{taxi_cost_day:.2f}')
elif kilometers < 20 and day_or_night == 'night':
    print(f'{taxi_cost_night:.2f}')
elif kilometers < 100:
    print(f'{autobus_cost:.2f}')
else:
    print(f'{train_cost:.2f}')

