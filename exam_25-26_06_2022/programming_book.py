pages_print_price = float(input())
covers_print_price = float(input())
percent_discount_paper = int(input())
design_price = float(input())
percent_team_payed = int(input())

pages_count = 899
covers_count = 2

initial_sum = pages_print_price * pages_count + covers_print_price * covers_count
discount = initial_sum * percent_discount_paper / 100

initial_sum = initial_sum - discount

total_sum = initial_sum + design_price

team_payed = total_sum * percent_team_payed / 100

final_sum = total_sum - team_payed

print(f"Avtonom should pay {final_sum:.2f} BGN.")
