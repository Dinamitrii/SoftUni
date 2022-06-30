destination = input()
while destination != "End":
    needed_money = float(input())
    collected_money = 0
    while collected_money < needed_money:
        current_money = float(input())
        collected_money += current_money
    print(f"Going to {destination}!")
    destination = input()
