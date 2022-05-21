fuel = input()  # Gas,Gasoline,Diesel
liters = float(input())
club_card = input()  # Yes,No

price_gas = 0.93
price_gasoline = 2.22
price_diesel = 2.33

gas_cost = liters * price_gas
gasoline_cost = liters * price_gasoline
diesel_cost = liters * price_diesel

if fuel == "Gas" or fuel == "Gasoline" or fuel == "Diesel":
    if club_card == "Yes":
        if 20 <= liters <= 25:
