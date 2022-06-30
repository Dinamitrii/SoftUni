needed_money = float(input())
init_money = float(input())

count_spend_days = 0
all_days_count = 0

while init_money < needed_money:
    if count_spend_days == 5:
        break
    action = input()
    amount = float(input())
    all_days_count += 1

    if action == "spend":
        count_spend_days += 1
        init_money -= amount
        if init_money < 0:
            init_money = 0
    elif action == "save":
        count_spend_days = 0
        init_money += amount

print()
