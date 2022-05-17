deposit = float(input())
monts = int(input())
interest = float(input()) / 100

interest_sum = deposit * interest
interest_mont = interest_sum / 12

total = deposit + monts * interest_mont

print(total)
