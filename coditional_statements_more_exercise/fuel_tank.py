fuel = input()  # Diesel, Gasoline , Gas
liters = float(input())
if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if liters >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print("Invalid fuel!")
