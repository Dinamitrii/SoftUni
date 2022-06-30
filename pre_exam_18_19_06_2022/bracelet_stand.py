pocket_money = float(input())
sales_money = float(input())
expences = float(input())
gift_price = float(input())

days_left = 5

pocket_savings = pocket_money * days_left
sales_savings = sales_money * days_left

total_savings = (pocket_savings + sales_savings) - expences

if total_savings >= gift_price:
    print(f"Profit: {total_savings:.2f} BGN, the gift has been purchased.")
else:
    diff = abs(gift_price - total_savings)
    print(f"Insufficient money: {diff:.2f} BGN.")
